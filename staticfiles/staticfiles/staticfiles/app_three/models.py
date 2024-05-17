from django.db import models
import uuid


class College(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True, unique=True)
    college_name = models.CharField(max_length=100, blank=False, null=True, unique=True)

    class Meta:
        verbose_name = 'College'
        verbose_name_plural = 'Colleges'

    def __str__(self):
        return self.college_name
    

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True, unique=True)
    school_name = models.CharField(max_length=100, blank=False, null=True, unique=True)
    college = models.ForeignKey('College', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'

    def __str__(self):
        return self.school_name


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True, unique=True)
    department_name = models.CharField(max_length=100, blank=False, null=True, unique=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    
    def __str__(self):
        return self.department_name


class Program(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True, unique=True)
    program_name = models.CharField(max_length=100, blank=False, null=True, unique=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    tuition = models.PositiveIntegerField(default=0, blank=True, null=True)

    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.program_name


class CourseUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True, unique=True)
    course_name = models.CharField(max_length=100, blank=False, null=True)

    year_and_semester = (
        ('Year 1 Sem 1', 'Year 1 Sem 1'),
        ('Year 1 Sem 2', 'Year 1 Sem 2'),
        ('Year 2 Sem 1', 'Year 2 Sem 1'),
        ('Year 2 Sem 2', 'Year 2 Sem 2'),
        ('Year 3 Sem 1', 'Year 3 Sem 1'),
        ('Year 3 Sem 2', 'Year 3 Sem 2'),
        ('Year 4 Sem 1', 'Year 4 Sem 1'),
        ('Year 4 Sem 2', 'Year 4 Sem 2'),
        ('Year 5 Sem 1', 'Year 5 Sem 1'),
        ('Year 5 Sem 2', 'Year 5 Sem 2'),
    )

    taught_in = models.CharField(max_length=100, choices=year_and_semester, blank=True)
    program = models.ForeignKey('Program', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Course Unit'
        verbose_name_plural = 'Course Units'

    def __str__(self):
        return self.course_name


class Room(models.Model):
    
    room_name = models.CharField(max_length=200)

    TABLES = 'Tables'
    SINGLE_SEATS = 'Single Seats'
    SELECT = 'Select'

    room_has = (
        (SELECT, 'Select'),
        (TABLES, 'Tables'),
        (SINGLE_SEATS, 'Single Seats'),
    )

    tables_or_single_seats = models.CharField(max_length=20, choices=room_has, default=SELECT)

    total_tables = models.PositiveIntegerField(default=0, blank=True, null=True)
    total_seats = models.PositiveIntegerField(default=0, blank=True, null=True)

    def room_has_tables(self):
        return self.tables_or_single_seats == self.TABLES
    
    def room_has_single_seats(self):
        return self.tables_or_single_seats == self.SINGLE_SEATS

    def __str__(self):
        return self.room_name

class Timetable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, auto_created=True)
    date = models.DateField(blank=False, null=True, default='2022-12-12')
    time_slot_choices = (
        ('8am-11am', '8am to 11am'),
        ('9am-12pm', '9am to 12pm'),
        ('1pm-4pm', '1pm to 4pm'),
        ('2pm-5pm', '2pm to 5pm'),
        ('5pm-7pm', '5pm to 7pm'),
    )
    time_slot = models.CharField(max_length=20, choices=time_slot_choices)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    course_name = models.ForeignKey(CourseUnit, on_delete=models.CASCADE)
    venue_or_room = models.ManyToManyField(Room, blank=True)

    class Meta:
        verbose_name = 'Timetable Entry'
        verbose_name_plural = 'Timetable Entries'

    def __str__(self):
        return f"{self.date} - {self.time_slot}"