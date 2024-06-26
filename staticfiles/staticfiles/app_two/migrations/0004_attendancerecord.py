# Generated by Django 5.0.1 on 2024-01-26 12:45

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_three', '0004_alter_timetable_venue_or_room'),
        ('app_two', '0003_student_paid_tution_student_registered_course_units'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_two.student')),
                ('timetable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_three.timetable')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
            },
        ),
    ]
