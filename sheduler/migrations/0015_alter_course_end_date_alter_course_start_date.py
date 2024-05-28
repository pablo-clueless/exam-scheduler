# Generated by Django 5.0.3 on 2024-05-26 10:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheduler', '0014_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
    ]