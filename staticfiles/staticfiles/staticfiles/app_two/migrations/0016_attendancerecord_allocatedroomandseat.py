# Generated by Django 5.0.1 on 2024-03-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0015_remove_attendancerecord_timetable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancerecord',
            name='allocatedRoomAndSeat',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
