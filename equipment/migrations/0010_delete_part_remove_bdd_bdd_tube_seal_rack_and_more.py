# Generated by Django 4.1.1 on 2022-10-19 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0009_rename_pressure_senser_pressure_sensor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.RemoveField(
            model_name='bdd',
            name='BDD_tube_seal_rack',
        ),
        migrations.RemoveField(
            model_name='calibration_stand',
            name='cal_stand_size',
        ),
        migrations.RemoveField(
            model_name='calibration_stand',
            name='calibration_orifice_set',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='TTD_tube_seal_rack',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='pressure_sensor',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='supply_orifice_set',
        ),
        migrations.DeleteModel(
            name='BDD_tube_seal_rack',
        ),
        migrations.DeleteModel(
            name='Calibration_orifice',
        ),
        migrations.DeleteModel(
            name='Pressure_sensor',
        ),
        migrations.DeleteModel(
            name='Supply_orifice',
        ),
        migrations.DeleteModel(
            name='TTD_tube_seal_rack',
        ),
    ]
