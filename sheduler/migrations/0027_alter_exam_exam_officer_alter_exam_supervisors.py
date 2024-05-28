# Generated by Django 5.0.3 on 2024-05-26 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0026_remove_course_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_officer',
            field=models.ForeignKey(limit_choices_to={'role': 'exam_officer'}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='exams_assigned', to='sheduler.examofficerprofile'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='supervisors',
            field=models.ManyToManyField(limit_choices_to={'role': 'supervisor'}, related_name='exams_supervised', to='sheduler.supervisorprofile'),
        ),
    ]
