# Generated by Django 5.0.3 on 2024-03-29 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0002_rename_name_course_course_name_customuser_full_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentenrollment',
            old_name='student',
            new_name='student_name',
        ),
        migrations.RenameField(
            model_name='supervisorassignment',
            old_name='supervisor',
            new_name='supervisor_name',
        ),
        migrations.AddField(
            model_name='studentenrollment',
            name='stuent_reg_number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisorassignment',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sheduler.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisorassignment',
            name='employee_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supervisorassignment',
            name='job_title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ExamOfficerAssignment',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('employee_id', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheduler.department')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sheduler.exam')),
                ('exam_officer_name', models.ForeignKey(limit_choices_to={'role': 'supervisor'}, on_delete=django.db.models.deletion.DO_NOTHING, to='sheduler.customuser')),
            ],
        ),
    ]
