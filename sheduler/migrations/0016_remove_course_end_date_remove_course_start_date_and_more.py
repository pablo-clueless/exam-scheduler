# Generated by Django 5.0.3 on 2024-05-26 10:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0015_alter_course_end_date_alter_course_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.AddField(
            model_name='course',
            name='date_addedd',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
