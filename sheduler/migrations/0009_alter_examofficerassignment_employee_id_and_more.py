# Generated by Django 5.0.3 on 2024-03-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0008_alter_examattendance_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examofficerassignment',
            name='employee_id',
            field=models.CharField(blank=True, default='123456', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='examofficerassignment',
            name='job_title',
            field=models.CharField(blank=True, default='123456', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supervisorassignment',
            name='employee_id',
            field=models.CharField(blank=True, default='123456', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='supervisorassignment',
            name='job_title',
            field=models.CharField(blank=True, default='123456', max_length=20, null=True),
        ),
    ]
