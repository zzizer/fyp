# Generated by Django 5.0.1 on 2024-02-09 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_two', '0010_alter_student_fingerprint_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fingerprint_location',
        ),
        migrations.AddField(
            model_name='student',
            name='fingerprint_encoding',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
