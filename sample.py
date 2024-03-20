from SPECIAL.timetable_entries_for_current_date import get_timetable_entries_for_current_date
from datetime import date
from SPECIAL.connect_to_database import connect_to_database, close_database_connection
from datetime import datetime


data_for_today = get_timetable_entries_for_current_date()

if data_for_today:

    entries = len(data_for_today)
    print(f'Units Today: {entries}')

    current_time = datetime.now().time()

    if current_time >= datetime.strptime('14:00', '%H:%M').time() and current_time <= datetime.strptime('18:00', '%H:%M').time():
        time_slot = '2pm-5pm'
    elif current_time >= datetime.strptime('07:00', '%H:%M').time() and current_time <= datetime.strptime('13:50', '%H:%M').time():
        time_slot = '9am-12pm'

    course_units = []

    for entry in data_for_today:
        if entry['time_slot'] == time_slot:
            course_units.append(entry['course_name'])

    units_number = len(course_units)
    print(f'Units for {time_slot}: {units_number}')

    unique_units = set(course_units)
    if len(unique_units) > 1:
        print("Units are different.")
        room_share = 2
        print("Rooms Allocated:")
        for unit in unique_units:
            shared_room = None
            for entry in data_for_today:
                if entry['course_name'] == unit:
                    if shared_room is None:
                        shared_room = entry['venue_or_room']
                    elif shared_room != entry['venue_or_room']:
                        shared_room = None
                        break
            if shared_room is not None:
                print(f"{unit}: {shared_room}")
    else:
        print("Units are the same.")
        room_share = 1
        shared_room = None
        for entry in data_for_today:
            if entry['course_name'] == course_units[0]:
                if shared_room is None:
                    shared_room = entry['venue_or_room']
                elif shared_room != entry['venue_or_room']:
                    shared_room = None
                    break
        if shared_room is not None:
            print(f"{course_units[0]}: {shared_room}")

    print(f"Room Share: {room_share}")

else:
    print("No data for today.")