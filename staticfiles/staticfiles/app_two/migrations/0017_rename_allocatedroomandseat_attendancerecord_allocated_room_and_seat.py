# Generated by Django 5.0.1 on 2024-03-06 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0016_attendancerecord_allocatedroomandseat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendancerecord',
            old_name='allocatedRoomAndSeat',
            new_name='allocated_room_and_seat',
        ),
    ]
