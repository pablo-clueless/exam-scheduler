# Generated by Django 5.0.3 on 2024-05-26 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0018_remove_course_deapartment_remove_course_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deapartment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sheduler.department'),
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='sheduler.faculty'),
        ),
    ]
