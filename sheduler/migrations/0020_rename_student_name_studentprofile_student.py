# Generated by Django 5.0.3 on 2024-05-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0019_course_deapartment_course_faculty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='student_name',
            new_name='student',
        ),
    ]
