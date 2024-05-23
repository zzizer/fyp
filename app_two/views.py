from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student, AttendanceRecord
import cv2
import face_recognition
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib import messages
from LCD.display import DisplayOnLCD
import time
from pyfingerprint.pyfingerprint import PyFingerprint, FINGERPRINT_CHARBUFFER1, FINGERPRINT_CHARBUFFER2
from SPECIAL.comparison import comparison
from django.contrib.messages.views import SuccessMessageMixin
from .forms import StudentUpdateForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from app_three.models import College, School, Program, Department, CourseUnit, Room, Timetable
from .analytics import calculate_total_attendance, calculate_attendance_rate, calculate_gender_attendance_rate, calculate_students_with_tution_balance, calculate_students_under_privilleged_access, calculate_students_with_zero_balance

def attendance_dashboard(request):

    attendance = AttendanceRecord.objects.all()
    registration_number = request.GET.get('filter_field')

    if registration_number:
        attendance = attendance.filter(student__registration_number=registration_number)

    context = {
        'attendance': attendance
    }

    return render(request, 'app_two/Attendance/attendance_dashboard.html', context)

@login_required(login_url='signin')
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect(reverse('student_details', args=[id]))
    else:
        form = StudentUpdateForm(instance=student)

    return render(request, 'app_two/Student/student_update.html', {'form': form, 'student': student})

@login_required(login_url='signin')
def generate_face_encoding(request, id):
    student = Student.objects.get(id=id)

    if student.photo and not student.face_encoding:
        # Use OpenCV for face detection
        image_path = student.photo.path
        image = cv2.imread(image_path)
        
        # Convert the image to RGB (as required by face_recognition)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Use face_recognition to locate faces using HOG-based model
        face_locations = face_recognition.face_locations(rgb_image, model="hog")

        if face_locations:
            # Assuming only one face, take the first face found
            top, right, bottom, left = face_locations[0]

            # Generate face encoding
            encodings = face_recognition.face_encodings(rgb_image, known_face_locations=[(top, right, bottom, left)])

            if encodings:
                encoding = encodings[0]

                # Store the encoding as bytes in the database
                student.face_encoding = encoding.tobytes()
                student.save()

    return redirect(reverse('student_details', args=[id]))

@login_required(login_url='signin')
def student_details(request, id):

    student = Student.objects.get(id=id)

    content = {
        'student': student
    }

    return render(request, 'app_two/Student/student_details.html', content)

@login_required(login_url='signin')
def all_students(request):
    students = Student.objects.all()

    content = {
        'students': students
    }

    return render(request, 'app_two/Student/all_students.html', content)

@login_required(login_url='signin')
def scan_save_fingerprint(request, id):
    try:
        student = Student.objects.get(id=id)

        display = DisplayOnLCD()

        f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

        if not f.verifyPassword():
            raise ValueError('The given fingerprint sensor password is wrong!')

        display.random_message('Place Finger')
        time.sleep(4)

        while not f.readImage():
            pass

        f.convertImage(FINGERPRINT_CHARBUFFER1)
        charactertics1 = f.downloadCharacteristics(FINGERPRINT_CHARBUFFER1)

        display.random_message('Remove Finger...')
        
        time.sleep(4)

        display.random_message('Place Finger Again...')

        while not f.readImage():
            pass

        f.convertImage(FINGERPRINT_CHARBUFFER2)
        charactertics2 = f.downloadCharacteristics(FINGERPRINT_CHARBUFFER2)

        if comparison(charactertics1, charactertics2) > 70:
            display.random_message('Meet 70% Match')

            fingerprint_xtics1 = charactertics1
            fingerprint_xtics2 = charactertics2

            student.fingerprint_xtics1 = fingerprint_xtics1
            student.fingerprint_xtics2 = fingerprint_xtics2

            student.save()
            
            time.sleep(2)
            display.random_message('Fingerprint Saved')

            return redirect(reverse('student_details', args=[id]))
        else:
            messages.warning(request, 'Fingers do not match. Please try again.')
            time.sleep(2)
            messages.error(request, f"Fingerprint match is {comparison(charactertics1, charactertics2)}%")
            display.random_message("Don't Meet 70% Match")
            return redirect(reverse('student_details', args=[id]))

    except Exception as e:
        messages.error(request, f'Operation failed! Exception message: {str(e)}')
        display.random_message('Operation failed')
        return redirect(reverse('student_details', args=[id]))

def analytics(request):
    course_units = CourseUnit.objects.all()
    with_zero_balance = calculate_students_with_zero_balance()
    under_privilleged_access = calculate_students_under_privilleged_access()
    with_tution_balance = calculate_students_with_tution_balance()
    
    total_students = Student.objects.all()
    total_students = len(total_students)

    selected_course_unit = None
    
    if request.method == 'POST':
        selected_course_unit_id = request.POST.get('course_unit_id')
        selected_course_unit = CourseUnit.objects.get(id=selected_course_unit_id)
        
        total_attendance = calculate_total_attendance(selected_course_unit)
        attendance_rate = calculate_attendance_rate(selected_course_unit)
        male_attendance_rate, female_attendance_rate = calculate_gender_attendance_rate(selected_course_unit)

        context = {
            'course_units': course_units,
            'selected_course_unit': selected_course_unit,
            'total_attendance': total_attendance,
            'attendance_rate': attendance_rate,
            'male_attendance_rate': male_attendance_rate,
            'female_attendance_rate': female_attendance_rate,
        }
        return render(request, 'app_two/Attendance/analytics.html', context)
    
    context = {
        'course_units': course_units,
        'under_privilleged_access': under_privilleged_access,
        'with_zero_balance': with_zero_balance,
        'total_students': total_students,
        'with_tution_balance': with_tution_balance,    
    }

    return render(request, 'app_two/Attendance/analytics.html', context)