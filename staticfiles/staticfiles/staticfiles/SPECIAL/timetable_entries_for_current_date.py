from datetime import date
from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from LCD.display import DisplayOnLCD

display = DisplayOnLCD()

def get_timetable_entries_for_current_date():
    current_date = date.today()

    # Connect to the PostgreSQL database
    connection = connect_to_database()

    try:
        if connection:
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()

            # Execute the SQL query to check if there are timetable entries for the current date
            cursor.execute("""
                SELECT id, program_id, course_name_id, time_slot
                FROM app_three_timetable
                WHERE date = %s
            """, (current_date,))

            # Fetch all rows
            rows = cursor.fetchall()

            if rows:
                # Extract program, course_name, and venue_or_room from each row
                data = []
                for row in rows:
                    timetable_id, program_id, course_name_id, time_slot = row

                    # Fetch venue_or_room using a separate query for each entry
                    cursor.execute("""
                        SELECT room_id
                        FROM app_three_timetable_venue_or_room
                        WHERE timetable_id = %s
                    """, (timetable_id,))

                    room_ids = cursor.fetchall()

                    venue_or_room = [room_id[0] for room_id in room_ids]

                    data.append({
                        'program': program_id,
                        'course_name': course_name_id,
                        'venue_or_room': venue_or_room,
                        'time_slot': time_slot,
                    })

                return data
                # print(f'Data: {data}')

            else:
                print("No timetable entries found for the current date.")
                display.random_message("No Exam Today.!")
                return None

    finally:
        close_database_connection(connection)


def has_registered_for_current_date(student_id, registered_course_units):
    current_date = date.today()

    # Get the timetable entries for the current date
    timetable_entries = get_timetable_entries_for_current_date()

    if timetable_entries:
        for entry in timetable_entries:
            # Check if the student has registered for the course unit in the timetable entry
            if entry['course_name'] in registered_course_units:
                # print(f"Taking Place units: {entry['course_name']}")
                return True, entry['course_name'], entry['venue_or_room']
            else:
                display.random_message("Not Registered for the unit..!")

    return False
