from app_two.models import Student, AttendanceRecord

def calculate_total_attendance(course_unit):
    return AttendanceRecord.objects.filter(course_unit=course_unit).count()

def calculate_attendance_rate(course_unit):
    total_students = Student.objects.count()
    attendance_records = AttendanceRecord.objects.filter(course_unit=course_unit)
    total_attendance = attendance_records.count()
    
    return (total_attendance / total_students) * 100

def calculate_gender_attendance_rate(course_unit):
    total_students = Student.objects.count()
    male_students = Student.objects.filter(gender='Male')
    female_students = Student.objects.filter(gender='Female')
    
    male_attendance_records = AttendanceRecord.objects.filter(course_unit=course_unit, student__in=male_students)
    female_attendance_records = AttendanceRecord.objects.filter(course_unit=course_unit, student__in=female_students)
    
    male_attendance_rate = (male_attendance_records.count() / male_students.count()) * 100
    female_attendance_rate = (female_attendance_records.count() / female_students.count()) * 100
    
    return male_attendance_rate, female_attendance_rate
