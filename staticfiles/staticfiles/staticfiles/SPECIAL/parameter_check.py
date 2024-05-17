from SPECIAL.connect_to_database import connect_to_database, close_database_connection

def parameter_check(student_id):
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor()
            
            # Fetch the program_id for the given student_id
            cursor.execute("SELECT program_id FROM public.app_two_student WHERE id = %s", (student_id,))
            program_id_result = cursor.fetchone()

            if program_id_result:
                program_id = program_id_result[0]

                # Fetch other information based on the program_id
                cursor.execute("SELECT registration_number, privilleged_access, paid_tuition FROM public.app_two_student WHERE id = %s", (student_id,))
                result = cursor.fetchone()

                if result:
                    registration_number, privileged_access, paid_tuition = result

                    # Fetch tuition data for the program
                    cursor.execute("SELECT tuition FROM public.app_three_program WHERE id = %s", (program_id,))
                    program_data = cursor.fetchone()

                    if program_data:
                        tuition_meant = program_data[0]

                        # Check tuition balance
                        balance = tuition_meant - paid_tuition

                        # Fetch registered course units for the student
                        cursor.execute("""
                            SELECT courseunit_id
                            FROM app_two_student_registered_course_units
                            WHERE student_id = %s
                        """, (student_id,))
                        registered_course_units = [row[0] for row in cursor.fetchall()]
                        # print(registered_course_units)
                        return privileged_access, registration_number, balance, registered_course_units
                    else:
                        print("Program data not found.")
            else:
                print("Program ID not found for the given student.")
        finally:
            if connection:
                close_database_connection(connection)

    return False, None, None, None
