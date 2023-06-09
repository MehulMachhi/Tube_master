# Generated by Django 4.1.1 on 2022-11-15 10:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_chemical_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='equipment_delivery_client',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='equipment_delivery_tubemaster',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='equipment_prep',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='equipment_ready',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='equipment_return_tubemaster',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='equipment_ship_client',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_end',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
