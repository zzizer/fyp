from LCD.display import DisplayOnLCD
from time import sleep
from SPECIAL.comparison import comparison
from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from pyfingerprint.pyfingerprint import PyFingerprint, FINGERPRINT_CHARBUFFER1
from SPECIAL.timetable_entries_for_current_date import get_timetable_entries_for_current_date, has_registered_for_current_date
from SPECIAL.parameter_check import parameter_check
from SPECIAL.mark_attendance import mark_attendance
from datetime import date
from SPECIAL.fingerprint_detection_and_recognition import search_fingerprint

display = DisplayOnLCD()

def get_data_from_database():
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, surname, fingerprint_position FROM public.app_two_student")
                students = cursor.fetchall()
                return students
        except Exception as e:
            print(f"Error fetching data from the database: {str(e)}")
        finally:
            close_database_connection(connection)

    return None


def main():
    connection = None

    fingerprint_position_sensor = search_fingerprint()
    data = get_data_from_database()
    
    for student in data:
        stored_position = student[2]

        print(type(stored_position))
        print(type(fingerprint_position_sensor))

        if fingerprint_position_sensor==stored_position:
            student_id = student[0]
            
            privileged_access, registration_number, balance, registered_course_units = parameter_check(student_id)

            if privileged_access:
                match_found, course_unit_id, venue_or_room = has_registered_for_current_date(student_id, registered_course_units)

                if match_found:
                    # call the function to mark attendance
                    seat_and_room = mark_attendance(student_id, course_unit_id, venue_or_room)
                    display.on_success(registration_number, "Attendance-Recorded", seat_and_room)
                    break
                else:
                    display.on_failure("Not Registered For CourseUnit")
                    break

            elif balance == 0:
                match_found, course_unit_id, venue_or_room = has_registered_for_current_date(student_id, registered_course_units)

                if match_found:
                    # call the function to mark attendance
                    seat_and_room = mark_attendance(student_id, course_unit_id, venue_or_room)
                    display.on_success(registration_number, "Attendance-Recorded", seat_and_room)
                    break

                else:
                    display.on_failure("Not Registered For CourseUnit")
                    break
                
            elif balance != 0:
                display.on_failure(f"Unpaid Tuition Balance: {balance}")
                break

    if connection:
        close_database_connection(connection)
