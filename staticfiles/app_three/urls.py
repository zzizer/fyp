from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('manage_all/', views.manage_all, name='manage_all'),
    path('timetable', views.timetable, name='timetable'),

    path('add_college_manually/', views.add_college_manually, name='add_college_manually'),
    path('add_school_manually/', views.add_school_manually, name='add_school_manually'),
    path('add_department_manually/', views.add_department_manually, name='add_department_manually'),
    path('add_program_manually/', views.add_program_manually, name='add_program_manually'),
    path('add_courseunit_manually/', views.add_courseunit_manually, name='add_courseunit_manually'),
    path('add_room_manually/', views.add_room_manually, name='add_room_manually'),
    path('add_tt_entry_manually/', views.add_tt_entry_manually, name='add_tt_entry_manually'),

    path('add_college_from_csv/', views.add_college_from_csv, name='add_college_from_csv'),
    path('add_school_from_csv/', views.add_school_from_csv, name='add_school_from_csv'),
    path('add_department_from_csv/', views.add_department_from_csv, name='add_department_from_csv'),
    path('add_program_from_csv/', views.add_program_from_csv, name='add_program_from_csv'),
    path('add_courseunit_from_csv/', views.add_courseunit_from_csv, name='add_courseunit_from_csv'),
    path('add_rooms_from_csv', views.add_rooms_from_csv, name='add_rooms_from_csv'),
    path('add_timetable_from_csv', views.add_timetable_from_csv, name='add_timetable_from_csv'),    
]
