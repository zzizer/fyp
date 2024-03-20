from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from datetime import datetime, date
from LCD.display import DisplayOnLCD
from time import sleep
from SPECIAL.seat_allocation1 import generate_seat_allocation

display = DisplayOnLCD()

def mark_attendance(student_id, course_unit_id, venue_or_room):
    connection = connect_to_database()

    if connection:
        try:
            with connection.cursor() as cursor:
                # Determine the current date and time within the function
                current_date = date.today()
                current_time = datetime.now().time()

                # Generate seat allocation
                seat_and_room = generate_seat_allocation(course_unit_id, venue_or_room)

                existing_attendance_query = "SELECT id, allocated_room_and_seat FROM public.app_two_attendancerecord WHERE student_id = %s AND course_unit_id = %s AND date = %s"
                cursor.execute(existing_attendance_query, (student_id, course_unit_id, current_date))
                existing_attendance = cursor.fetchone()

                if not existing_attendance:
                    # Exclude 'id' from the list of columns for which values are provided
                    insert_query = "INSERT INTO public.app_two_attendancerecord (student_id, course_unit_id, date, time, allocated_room_and_seat) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(insert_query, (student_id, course_unit_id, current_date, current_time, seat_and_room))

                    connection.commit()

                    print(f"Attendance successfully marked for student {student_id} on {current_date} for course unit {course_unit_id}")
                    return seat_and_room
                    
                else:
                    display.random_message("Attendance already marked")
                    sleep(2)
                    print(f"Attendance already marked for student {student_id} on {current_date} for course unit {course_unit_id}")
                    return existing_attendance[1]  # Use index 1 to retrieve allocated_room_and_seat

        except Exception as e:
            print(f"Error marking attendance: {str(e)}")
        finally:
            close_database_connection(connection)
