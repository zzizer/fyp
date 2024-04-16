import random
from SPECIAL.seat_allocation_logic import room_analysis
from SPECIAL.connect_to_database import connect_to_database, close_database_connection

def unique_seat_generation(all_seats, room_name):
    # Randomly choose a seat number and a room
    random_seat = random.choice(all_seats)
    random_room = random.choice([room_name])

    # Concatenate them to create the seat allocation
    seat_allocation = f'{random_room}-{random_seat}'

    print(f"seat_allocation: {seat_allocation}")

    return seat_allocation

def generate_seat_allocation(course_unit_id, venue_or_room):

    all_seats, room_name = room_analysis(course_unit_id, venue_or_room[0])

    connection = connect_to_database()

    if connection:
        try:
            with connection.cursor() as cursor:

                seat_allocation = True

                while seat_allocation:
                    
                    possible_seat = unique_seat_generation(all_seats, room_name)

                    seat_allocation_query = "SELECT allocated_room_and_seat FROM public.app_two_attendancerecord WHERE allocated_room_and_seat = %s"
                    cursor.execute(seat_allocation_query, (possible_seat,))
                    seat_allocation = cursor.fetchone()

                    # print(f"seat_allocation: {seat_allocation}")
                    # if seat_allocation==None:
                    #     seat_allocation = False

                    if seat_allocation != None:
                        continue
                    
                    return possible_seat                       

        except Exception as e:
            print(f"Error generating seat allocation: {str(e)}")
        finally:
            close_database_connection(connection)