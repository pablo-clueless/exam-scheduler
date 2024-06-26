# Generated by Django 5.0.3 on 2024-03-29 21:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0007_rename_stuent_reg_number_studentenrollment_student_reg_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examattendance',
            name='student',
            field=models.ForeignKey(limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendances', to='sheduler.customuser'),
        ),
        migrations.AlterField(
            model_name='examofficerassignment',
            name='exam_officer_name',
            field=models.ForeignKey(limit_choices_to={'role': 'exam_officer'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exam_officer_assignments', to='sheduler.customuser'),
        ),
        migrations.AlterField(
            model_name='studentenrollment',
            name='student_name',
            field=models.ForeignKey(limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='enrollments', to='sheduler.customuser'),
        ),
        migrations.AlterField(
            model_name='supervisorassignment',
            name='supervisor_name',
            field=models.ForeignKey(limit_choices_to={'role': 'supervisor'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='supervisor_assignments', to='sheduler.customuser'),
        ),
    ]
