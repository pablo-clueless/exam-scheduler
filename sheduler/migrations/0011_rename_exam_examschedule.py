# Generated by Django 5.0.3 on 2024-04-04 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0010_rename_examofficerassignment_examofficerprofile_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Exam',
            new_name='ExamSchedule',
        ),
    ]
