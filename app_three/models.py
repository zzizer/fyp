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
    
    def available_table_seats(self, num_programs):
        if not self.room_has_tables():
            return None

        total_seats = self.total_tables * 3
        allocated_seats = set()

        available_seats_by_program = {}

        for program in range(1, num_programs + 1):
            available_seats = set()
            if program == 1:
                # Program 1, allocate seats to the ends of the tables, leaving the middle seat free
                for i in range(self.total_tables):
                    available_seats.update(set(range(i * 3 + 1, (i + 1) * 3 + 1, 2)) - allocated_seats)
            elif program == 2:
                # For program 2, allocate seats to the middle of the tables
                for i in range(self.total_tables):
                    available_seats.update(set(range(i * 3 + 2, (i + 1) * 3 + 1, 3)) - allocated_seats)
            elif program == 3:
                # For program 3, allocate remaining seats on the tables
                for i in range(self.total_tables):
                    remaining_seats = set(range(i * 3 + 1, (i + 1) * 3 + 1)) - allocated_seats
                    # Assign one seat per program in a round-robin manner
                    available_seats.update(list(remaining_seats)[program - 1::num_programs])

            allocated_seats.update(available_seats)
            available_seats_by_program[program] = list(available_seats)

        return available_seats_by_program

    def available_single_seats(self, num_programs):
        if not self.room_has_single_seats():
            return None

        total_seats = self.total_seats if self.total_seats is not None else 0
        total_students = num_programs  # Assuming one student per program

        if total_students > total_seats:
            raise ValueError("Not enough single seats for all students")

        # Return all available single seats
        available_seats = list(range(1, total_seats + 1))

        return available_seats

    def save(self, *args, **kwargs):
        # Dynamically set total_seats or total_tables to None based on the selected option
        if self.tables_or_single_seats == self.SELECT:
            self.total_seats = None
            self.total_tables = None
        elif self.room_has_tables():
            self.total_seats = None

        super().save(*args, **kwargs)

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