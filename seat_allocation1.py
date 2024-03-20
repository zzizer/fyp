import random
from better import room_analysis


def generate_seat_allocation():

    venue_or_room = 12
    course_unit_id = '5f5441e1-a855-4618-9da9-1eeb1b4439f8'

    # print(f'course_unit_id: {course_unit_id}')

    sample = room_analysis(course_unit_id, venue_or_room)

    print(f'Sample: {sample}')

    
    rooms = ['room10']

    # Randomly choose a seat number and a room
    random_seat = random.choice(sample)
    random_room = random.choice(rooms)

    # Concatenate them to create the seat allocation
    seat_allocation = f'{random_room}-{random_seat}'

    return seat_allocation
    # return venue_or_room
    print(f'Seat allocation: {seat_allocation}')

print(generate_seat_allocation())
