import random
from SPECIAL.seat_allocation_logic import room_analysis

def generate_seat_allocation(course_unit_id, venue_or_room):

    # venue_or_room = 12
    # course_unit_id = '5f5441e1-a855-4618-9da9-1eeb1b4439f8'

    # print(f'course_unit_id: {course_unit_id}')
    # print(f'venue_or_room: {venue_or_room}')

    all_seats, room_name = room_analysis(course_unit_id, venue_or_room[0])

    # print(f'Sample: {sample}')

    
    # rooms = ['Room X']

    # Randomly choose a seat number and a room
    random_seat = random.choice(all_seats)
    random_room = random.choice([room_name])

    # Concatenate them to create the seat allocation
    seat_allocation = f'{random_room}-{random_seat}'

    return seat_allocation
    # return venue_or_room
    # print(f'Seat allocation: {seat_allocation}')

# print(generate_seat_allocation())
