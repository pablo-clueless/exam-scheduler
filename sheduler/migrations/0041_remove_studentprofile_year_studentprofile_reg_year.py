# Generated by Django 5.0.3 on 2024-06-06 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0040_studentprofile_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='year',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='reg_year',
            field=models.IntegerField(default=2021),
        ),
    ]
