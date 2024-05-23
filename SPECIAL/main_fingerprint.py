from LCD.display import DisplayOnLCD
from time import sleep
from SPECIAL.comparison import comparison
from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from pyfingerprint.pyfingerprint import PyFingerprint, FINGERPRINT_CHARBUFFER1
from SPECIAL.timetable_entries_for_current_date import get_timetable_entries_for_current_date, has_registered_for_current_date
from SPECIAL.parameter_check import parameter_check
from SPECIAL.mark_attendance import mark_attendance
from datetime import date

display = DisplayOnLCD()

def get_data_from_database():
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, surname, fingerprint_xtics1, fingerprint_xtics2 FROM public.app_two_student")
                students = cursor.fetchall()
                return students
        except Exception as e:
            print(f"Error fetching data from the database: {str(e)}")
        finally:
            close_database_connection(connection)

    return None

def main():
    connection = None  # Initialize the connection variable

    try:
        f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)
        if not f.verifyPassword():
            raise ValueError('The given fingerprint sensor password is wrong!')

        get_data_from_database()  # Establish a database connection within main

        display.random_message("Press Finger")
        sleep(3)

        while not f.readImage():
            pass

        f.convertImage(FINGERPRINT_CHARBUFFER1)
        scanned_xtics = f.downloadCharacteristics(FINGERPRINT_CHARBUFFER1)
        # print(scanned_xtics)

        data = get_data_from_database()

        for student in data:
            stored_characteristics1 = eval(student[2])
            stored_characteristics2 = eval(student[3])

            if comparison(scanned_xtics, stored_characteristics1) > 73 or comparison(scanned_xtics, stored_characteristics2) > 75:
                student_id = student[0]

                privileged_access, registration_number, balance, registered_course_units = parameter_check(student_id)
                
                # print(f'\nSpecial Access: {privileged_access}')
                # print(f'Reg No: {registration_number}')
                # print(f'Balance: {balance}')
                # print(f'Registered Units: {registered_course_units}\n')

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

            else: 
                display.random_message("Student Not Recognised")

    except Exception as e:
        print(f'Exception occurred: {str(e)}')
        exit(1)

    finally:
        if connection:
            close_database_connection(connection)

# if __name__ == "__main__":
#     main()
