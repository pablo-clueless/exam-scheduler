# Generated by Django 5.0.3 on 2024-05-27 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0031_alter_examattendance_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examattendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendances', to='sheduler.studentprofile'),
        ),
    ]
