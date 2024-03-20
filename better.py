from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from datetime import datetime, date
from SPECIAL.timetable_entries_for_current_date import get_timetable_entries_for_current_date


def room_with_tables_two_programs(total_tables):
    seats_per_tables = 3
    program1_seats = []
    program2_seats = []

    program1_seat = 1
    program2_seat = 2

    for table in range(total_tables):
        for seat in range(seats_per_tables):
            if seat == 0 or seat ==2:
                program1_seats.append(program1_seat)
                program1_seat += 2
            else:
                program2_seats.append(program2_seat)
                program2_seat += 2
    
    return program1_seats, program2_seats

# print(room_with_tables_two_programs(20))

# program1_seats, program2_seats = room_with_tables_two_programs(20)
# print(f'program1_seats: {program1_seats}\nprogram2_seats: {program2_seats}')

def room_with_tables_single_program(total_tables):
    seats_per_tables = 3
    program_seats = []

    program_seat = 1

    for table in range(total_tables):
        for seat in range(seats_per_tables):
            if seat == 0 or seat ==2:
                program_seats.append(program_seat)
                program_seat += 2
    
    return program_seats

# program_seats = room_with_tables_single_program(20)
# print(f'program_seats: {program_seats}')

def room_with_single_seats(total_seats):
    available_seats = list(range(1, total_seats+1))

    return available_seats

# available_seats = room_with_single_seats(20)
# print(f'available_seats: {available_seats}')

def analysis(course_unit_id, room_name):
    data_for_today = get_timetable_entries_for_current_date()

    entries = len(data_for_today)
    print(f'Units Today: {entries}')

    current_time = datetime.now().time()

    if current_time >= datetime.strptime('14:00', '%H:%M').time() and current_time <= datetime.strptime('18:00', '%H:%M').time():
        time_slot = '2pm-5pm'
    elif current_time >= datetime.strptime('07:00', '%H:%M').time() and current_time <= datetime.strptime('13:50', '%H:%M').time():
        time_slot = '9am-12pm'

    course_units = []
    room_ids = []

    for entry in data_for_today:
        if entry['time_slot'] == time_slot:
            course_units.append(entry['course_name'])
    
    for entry in data_for_today:
        room_ids.append(entry['venue_or_room'])

    # units_number = len(course_units)
    # print(f'Units for {time_slot}: {units_number}')

    units_number = room_ids.count([room_name])
    print(room_ids)
    # print(f'Units for {time_slot}: {units_number}')
    
    # print(room_ids)
    # pairs = zip(course_units, room_ids)
    # unit_room = (list(pairs))
    # print(f'unit_room: {unit_room}')

    # print(course_units)
    # print(room_ids)
    # print(units_number)

    return units_number, course_units, room_ids

# analysis()

def room_analysis(course_unit_id, room_name):

    course_unit_one = course_unit_id
    # print(f'course_unit_id: {course_unit_one}')

    connection = connect_to_database()
    units_number, course_units, room_ids= analysis(course_unit_id, room_name)
    # print(course_units[1])

    try:
        if connection:
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()

            cursor.execute("""
                SELECT id, tables_or_single_seats, total_tables, total_seats
                FROM app_three_room
                WHERE id = %s
            """, (room_name,))

            room_data = cursor.fetchall()
            print(f'room_data: {room_data}')
            
            if room_data[0][1] == 'Tables':
                if units_number == 2:
                    if course_units[0] != course_unit_one:
                        program1_seats, _ = room_with_tables_two_programs(room_data[0][2])
                        return program1_seats
                    elif course_units[1]:
                        _ , program2_seats = room_with_tables_two_programs(room_data[0][2])
                        return program2_seats

                elif units_number == 1:
                        program_seats = room_with_tables_single_program(room_data[0][2])
                        # print(f'program_seats: {program_seats}')
                        return program_seats
                else:
                    print('No available seats')
                    return 0

            elif room_data[0][1] == 'Single Seats':
                available_seats = room_with_single_seats(room_data[0][3])
                # print(f'available_seats: {available_seats}')
                return available_seats

    finally:
        close_database_connection(connection)
