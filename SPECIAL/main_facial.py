from SPECIAL.facial_detection_and_recognition import facial_detection_and_recognition
from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from SPECIAL.comparison import face_encoding_similarity
from LCD.display import DisplayOnLCD
from SPECIAL.timetable_entries_for_current_date import get_timetable_entries_for_current_date, has_registered_for_current_date
from SPECIAL.parameter_check import parameter_check
from SPECIAL.mark_attendance import mark_attendance

display = DisplayOnLCD()

def get_data_from_database():
    connection = connect_to_database()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, face_encoding FROM public.app_two_student")
                students = cursor.fetchall()
                return students
        except Exception as e:
            print(f"Error fetching data from the database: {str(e)}")
        finally:
            close_database_connection(connection)
    return None

def main1():
    try:
        data = get_data_from_database()

        if not data:
            display.on_failure("No student data found in database")
            return

        while True:
            scanned_face_encoding = facial_detection_and_recognition()

            if scanned_face_encoding is None:
                display.random_message("No face detected, please try again")
                continue

            for student in data:
                stored_face_encoding = student[1]

                if face_encoding_similarity(scanned_face_encoding, stored_face_encoding) > 55:
                    student_id = student[0]

                    privileged_access, registration_number, balance, registered_course_units = parameter_check(student_id)

                    if privileged_access:
                        match_found, course_unit_id, venue_or_room = has_registered_for_current_date(student_id, registered_course_units)

                        if match_found:
                            seat_and_room = mark_attendance(student_id, course_unit_id, venue_or_room)
                            display.on_success(registration_number, "Attendance Recorded", seat_and_room)
                            return
                        else:
                            display.on_failure("Not Registered for Course Unit")
                            return

                    if balance == 0:
                        match_found, course_unit_id, venue_or_room = has_registered_for_current_date(student_id, registered_course_units)

                        if match_found:
                            seat_and_room = mark_attendance(student_id, course_unit_id, venue_or_room)
                            display.on_success(registration_number, "Attendance Recorded", seat_and_room)
                            return
                        else:
                            display.on_failure("Not Registered for Course Unit")
                            return

                    if balance != 0:
                        display.on_failure(f"Unpaid Tuition Balance: {balance}")
                        return
                else:
                    display.random_message("Student Not Recognised")
                    continue
    except Exception as e:
        print(f'Exception occurred: {str(e)}')
        # display.on_failure(f"Exception: {str(e)}")

# if __name__ == "__main__":
#     main1()

# # main_facial.py
# from SPECIAL.facial_detection_and_recognition import facial_detection_and_recognition
# from SPECIAL.connect_to_database import connect_to_database, close_database_connection
# from SPECIAL.comparison import face_encoding_similarity
# import numpy as np
# from LCD.display import DisplayOnLCD
# from time import sleep
# from SPECIAL.comparison import comparison
# from SPECIAL.connect_to_database import connect_to_database, close_database_connection
# from SPECIAL.timetable_entries_for_current_date import get_timetable_entries_for_current_date, has_registered_for_current_date
# from SPECIAL.parameter_check import parameter_check
# from SPECIAL.mark_attendance import mark_attendance
# from datetime import date

# display = DisplayOnLCD()

# def get_data_from_database():
#     connection = connect_to_database()
#     if connection:
#         try:
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT id, face_encoding FROM public.app_two_student")
#                 students = cursor.fetchall()
#                 return students
#         except Exception as e:
#             print(f"Error fetching data from the database: {str(e)}")
#         finally:
#             close_database_connection(connection)

#     return None

# def main1():
#     connection=None

#     try:
#         get_data_from_database()

#         data = get_data_from_database()

#         for student in data:

#             scanned_face_encoding = facial_detection_and_recognition()

#             stored_face_encoding = student[1]
#             # print(f'stored_face_encoding: {stored_face_encoding}')
            
#             if face_encoding_similarity(scanned_face_encoding, stored_face_encoding) > 40:
#                 student_id = student[0]

#                 privileged_access, registration_number, balance, registered_course_units = parameter_check(student_id)

#                 if privileged_access:
#                     match_found, course_unit_id, venue_or_room = has_registered_for_current_date(student_id, registered_course_units)

#                     if match_found:
#                         # call the function to mark attendance
#                         seat_and_room = mark_attendance(student_id, course_unit_id, venue_or_room)
#                         display.on_success(registration_number, "Attendance-Recorded", seat_and_room)
#                         # print(f"Attendance-Recorded for {registration_number} at {seat_and_room}")
#                         break
#                     else:
#                         display.on_failure("Not Registered Courseunit")
#                         # print("Not Registered")
#                         break

#                 elif balance == 0:
#                     match_found, course_unit_id, venue_or_room = has_registered_for_current_date(student_id, registered_course_units)

#                     if match_found:
#                         # call the function to mark attendance
#                         seat_and_room = mark_attendance(student_id, course_unit_id, venue_or_room)
#                         display.on_success(registration_number, "Attendance-Recorded", seat_and_room)
#                         # print(f"Attendance-Recorded for {registration_number} at {seat_and_room}")
#                         break

#                     else:
#                         display.on_failure("Not Registered CourseUnit")
#                         # print("Not Registered")
#                         break
                
#                 elif balance != 0:
#                     display.on_failure(f"Unpaid Tuition Balance: {balance}")
#                     # print(f"Unpaid Tuition Balance: {balance}")
#                     break

#             else: 
#                 display.random_message("Student Not Recognised")
#                 print("Not Found. Try again.")
            
#     except Exception as e:
#         print(f'Exception occurred: {str(e)}')
#         exit(1)

#     finally:
#         if connection:
#             close_database_connection(connection)

# # if __name__ == "__main__":
# #     main()