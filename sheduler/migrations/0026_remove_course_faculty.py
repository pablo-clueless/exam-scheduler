# Generated by Django 5.0.3 on 2024-05-26 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0025_rename_deapartment_course_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='faculty',
        ),
    ]
