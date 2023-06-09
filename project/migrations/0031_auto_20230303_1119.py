# Generated by Django 3.2.16 on 2023-03-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0032_alter_bdd_tube_seal_rack_number_of_tubes'),
        ('project', '0030_auto_20230301_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='airhose_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.AirHose', verbose_name='Air Hose'),
        ),
        migrations.AddField(
            model_name='project',
            name='bdd_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.BDD_tube_seal_rack', verbose_name='BDD Tube Seal Rack'),
        ),
        migrations.AddField(
            model_name='project',
            name='calibration_orifice_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.Calibration_orifice', verbose_name='Calibration Orifice'),
        ),
        migrations.AddField(
            model_name='project',
            name='device_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.DeviceHose', verbose_name='Device Hose'),
        ),
        migrations.AddField(
            model_name='project',
            name='pressure_sensor_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.Pressure_sensor', verbose_name='Pressure Sensor'),
        ),
        migrations.AddField(
            model_name='project',
            name='supply_orifice_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.Supply_orifice', verbose_name='Supply Orifice'),
        ),
        migrations.AddField(
            model_name='project',
            name='swabmaster_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.SwabMasterTSR', verbose_name='Swab Master TSR'),
        ),
        migrations.AddField(
            model_name='project',
            name='ttd_part',
            field=models.ManyToManyField(blank=True, default='', null=True, to='part.TTD_tube_seal_rack', verbose_name='TTD tube Seal Rack'),
        ),
    ]
