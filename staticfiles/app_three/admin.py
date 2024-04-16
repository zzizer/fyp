from django.contrib import admin
from .models import College, School, Department, Program, CourseUnit, Timetable, Room

admin.site.register(College)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(CourseUnit)
admin.site.register(Timetable)
admin.site.register(Room)