# Generated by Django 4.1.1 on 2022-09-22 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0002_equipment_warehouse_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='warehouse_location',
        ),
        migrations.AddField(
            model_name='equipment',
            name='warehouse_location',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tube.warehouse', verbose_name='Warehouse Location'),
        ),
    ]
