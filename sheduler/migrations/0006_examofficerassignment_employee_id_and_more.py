# Generated by Django 5.0.3 on 2024-03-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0005_remove_examofficerassignment_employee_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examofficerassignment',
            name='employee_id',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='examofficerassignment',
            name='job_title',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='supervisorassignment',
            name='employee_id',
            field=models.CharField(default='123456', max_length=20),
        ),
        migrations.AddField(
            model_name='supervisorassignment',
            name='job_title',
            field=models.CharField(default='123456', max_length=20),
        ),
    ]
