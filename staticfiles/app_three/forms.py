from django import forms
from .models import College, School, Department, Program, CourseUnit, Timetable, Room

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name']

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name', 'college']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'school']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['program_name', 'department']

class CourseUnitForm(forms.ModelForm):
    class Meta:
        model = CourseUnit
        fields = ['course_name', 'taught_in', 'program']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_name', 'tables_or_single_seats', 'total_tables', 'total_seats']

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['date', 'time_slot', 'program', 'course_name', 'venue_or_room']