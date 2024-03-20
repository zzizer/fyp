from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CollegeForm, SchoolForm, DepartmentForm, ProgramForm, CourseUnitForm, RoomForm, TimetableForm
from .models import College, School, Department, Program, CourseUnit, Timetable, Room
import csv

def timetable(request):
    timetable = Timetable.objects.all()

    context = {
        'timetable': timetable
    }
    
    return render(request, 'app_three/timetable.html', context)

@login_required(login_url='signin')
def dashboard(request):

    return render(request, 'app_three/dashboard.html')

def add_college_manually(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CollegeForm()

    return render(request, 'app_three/add_college_manually.html', {'form': form})

def add_school_manually(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SchoolForm()

    return render(request, 'app_three/add_school_manually.html', {'form': form})

def add_department_manually(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DepartmentForm()

    return render(request, 'app_three/add_department_manually.html', {'form': form})

def add_program_manually(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProgramForm()

    return render(request, 'app_three/add_program_manually.html', {'form': form})

def add_courseunit_manually(request):
    if request.method == 'POST':
        form = CourseUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CourseUnitForm()

    return render(request, 'app_three/add_courseunit_manually.html', {'form': form})

def add_room_manually(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RoomForm()

    return render(request, 'app_three/add_room_manually.html', {'form': form})

def add_tt_entry_manually(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TimetableForm()

    return render(request, 'app_three/add_tt_entry_manually.html', {'form': form})

def add_college_from_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            College.objects.create(
                college_name=row['college_name']
            )

        return redirect('dashboard')

    return render(request, 'app_three/add_college_from_csv.html')

def add_school_from_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            # Extract data from the CSV row
            school_name = row.get('school_name', '')
            college_name = row.get('college', '')

            # Check if the College already exists or create a new one using the correct field
            college, created = College.objects.get_or_create(college_name=college_name)

            # Create the School using the College instance
            School.objects.create(
                school_name=school_name,
                college=college
            )

        return redirect('dashboard')

    return render(request, 'app_three/add_school_from_csv.html')


def add_department_from_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            # Extract data from the CSV row
            department_name = row.get('department_name', '')
            school_name = row.get('school', '')

            # Check if the School already exists or create a new one using the correct field
            school, created = School.objects.get_or_create(school_name=school_name)

            # Create the Department using the School instance
            Department.objects.create(
                department_name=department_name,
                school=school
            )

        return redirect('dashboard')

    return render(request, 'app_three/add_department_from_csv.html')



def add_program_from_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            # Extract data from the CSV row
            program_name = row.get('program_name', '')
            department_name = row.get('department', '')

            # Check if the Department already exists or create a new one using the correct field
            department, created = Department.objects.get_or_create(department_name=department_name)

            # Create the Program using the Department instance
            Program.objects.create(
                program_name=program_name,
                department=department
            )

        return redirect('dashboard')

    return render(request, 'app_three/add_program_from_csv.html')


def add_courseunit_from_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']

        decoded_file = csv_file.read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(decoded_file)

        for row in csv_reader:
            # Extract data from the CSV row
            course_name = row.get('course_name', '')
            taught_in = row.get('taught_in', '')
            program_name = row.get('program', '')

            # Check if the Program already exists or create a new one using the correct field
            program, created = Program.objects.get_or_create(program_name=program_name)

            # Create the CourseUnit using the Program instance
            CourseUnit.objects.create(
                course_name=course_name,
                taught_in=taught_in,
                program=program
            )

        return redirect('dashboard')

    return render(request, 'app_three/add_courseunit_from_csv.html')

def add_timetable_from_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        try:
            csv_file = request.FILES['csv_file']

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)

            for row in csv_reader:
                # Extract data from the CSV row
                date = row.get('date', '')
                time_slot = row.get('time_slot', '')
                program_name = row.get('program_name', '')
                course_name = row.get('course_name', '')
                room_name = row.get('room_name', '')

                # Check if the Room already exists or create a new one using the correct field
                room, created = Room.objects.get_or_create(room_name=room_name)

                # Retrieve the Program and CourseUnit instances
                program = Program.objects.get(program_name=program_name)
                course_unit = CourseUnit.objects.get(course_name=course_name)

                # Create the Timetable entry using the Room, Program, and CourseUnit instances
                timetable_entry = Timetable.objects.create(
                    date=date,
                    time_slot=time_slot,
                    program=program,
                    course_name=course_unit,
                )
                
                timetable_entry.venue_or_room.add(room)

            return redirect('dashboard')

        except csv.Error as e:
            # Handle CSV errors, you may want to log or display an error message to the user
            return render(request, 'app_three/add_timetable_from_csv.html', {'error_message': 'Error processing the CSV file.'})

        except Exception as e:
            # Handle other exceptions
            return render(request, 'app_three/add_timetable_from_csv.html', {'error_message': str(e)})

    return render(request, 'app_three/add_timetable_from_csv.html')

def add_rooms_from_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        try:
            csv_file = request.FILES['csv_file']

            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)

            for row in csv_reader:
                # Extract data from the CSV row
                room_name = row.get('room_name', '')
                tables_or_single_seats = row.get('tables_or_single_seats', '')
                total_tables = row.get('total_tables', 0)
                total_seats = row.get('total_seats', 0)

                # Create the Room using the extracted data
                Room.objects.create(
                    room_name=room_name,
                    tables_or_single_seats=tables_or_single_seats,
                    total_tables=total_tables,
                    total_seats=total_seats
                )

            return redirect('dashboard')

        except csv.Error as e:
            # Handle CSV errors, you may want to log or display an error message to the user
            return render(request, 'app_three/add_rooms_from_csv.html', {'error_message': 'Error processing the CSV file.'})

        except Exception as e:
            # Handle other exceptions
            return render(request, 'app_three/add_rooms_from_csv.html', {'error_message': str(e)})

    return render(request, 'app_three/add_rooms_from_csv.html')


def manage_all(request):

    manage = request.GET.get('model', None)
    items = None

    if manage == 'Room':
        items = Room.objects.all()
    elif manage == 'College':
        items = College.objects.all()
    elif manage == 'School':
        items = School.objects.all()
    elif manage == 'Department':
        items = Department.objects.all()
    elif manage == 'Program':
        items = Program.objects.all()
    elif manage == 'CourseUnit':
        items = CourseUnit.objects.all()
    elif manage == 'Timetable':
        items = Timetable.objects.all()
    else:
        items = 'Kindly select a field of interest.'

    context = {
        'items': items,
        # 'message':'Kindly select a field of interest.',
    }

    return render(request, 'app_three/manage_all.html', context)