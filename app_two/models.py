from django.db import models
import uuid
from app_three.models import Program, Timetable, CourseUnit
from django.urls import reverse

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)

    first_name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )

    gender = models.CharField(max_length=10, blank=True, null=True, choices=gender_choices)

    registration_number = models.CharField(max_length=30, blank=True, null=True)
    student_number = models.CharField(max_length=30, blank=True, null=True)

    program = models.ForeignKey(Program, on_delete=models.CASCADE, blank=True, null=True)

    photo = models.ImageField(blank=True, null=True)

    privilleged_access = models.BooleanField(default=False)
    face_encoding = models.TextField(blank=True, null=True)
        
    fingerprint_xtics1 = models.TextField(blank=True, null=True)
    fingerprint_xtics2 = models.TextField(blank=True, null=True)

    paid_tuition = models.PositiveIntegerField(default=0, blank=True, null=True)
    registered_course_units = models.ManyToManyField(CourseUnit, blank=True)

    def __str__(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.surname}"
            
        return f"{self.first_name} {self.surname} {self.middle_name}"
    
    class Meta:
        verbose_name_plural = 'Students'
        verbose_name = 'Student'

    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url
    
    def balance(self):
        return self.program.tuition - self.paid_tuition
    
    def get_absolute_url(self):
        return reverse('student_details', kwargs={'id': self.id})
    

class AttendanceRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    
    course_unit = models.ForeignKey(CourseUnit, on_delete=models.CASCADE, blank=True, null=True)
    # timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, blank=True, null=True)

    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    allocated_room_and_seat = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.student} {self.course_unit} {self.date} {self.time}"
    
    class Meta:
        verbose_name_plural = 'Attendances'
        verbose_name = 'Attendance'