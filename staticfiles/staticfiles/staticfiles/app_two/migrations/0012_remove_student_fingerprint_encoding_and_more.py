# Generated by Django 5.0.1 on 2024-02-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0011_remove_student_fingerprint_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fingerprint_encoding',
        ),
        migrations.AddField(
            model_name='student',
            name='fingerprint_xtics1',
            field=models.CharField(blank=True, max_length=900000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='fingerprint_xtics2',
            field=models.CharField(blank=True, max_length=900000, null=True),
        ),
    ]
