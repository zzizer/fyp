from django.urls import path
from . import views

urlpatterns = [

    path('generate_face_encoding/<uuid:id>/', views.generate_face_encoding, name='generate_face_encoding'),
    path('student_details/<uuid:id>/', views.student_details, name='student_details'),
    path('all_students/', views.all_students, name='all_students'),
    path('scan_save_fingerprint/<uuid:id>/', views.scan_save_fingerprint, name='scan_save_fingerprint'),
    path('update_student/<uuid:id>/', views.update_student, name='student_update'),
    path('attendance_dashboard', views.attendance_dashboard, name='attendance_dashboard'),
    path('attendance_statistics', views.analytics, name='attendance_statistics'),

]
