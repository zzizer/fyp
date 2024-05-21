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

def calculate_students_with_zero_balance():
    students = Student.objects.all()
    students_with_zero_balance = [student for student in students if student.balance() == 0]
    return len(students_with_zero_balance)

def calculate_students_under_privilleged_access():
    privileged_students = Student.objects.filter(privilleged_access=True)
    return privileged_students.count()

def calculate_students_with_tution_balance():
    students = Student.objects.all()
    students_with_balance = [student for student in students if student.balance() > 0]
    return len(students_with_balance)
