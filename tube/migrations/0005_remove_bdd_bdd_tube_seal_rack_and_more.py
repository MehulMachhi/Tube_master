# Generated by Django 4.1.1 on 2022-10-14 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0004_delete_equipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdd',
            name='BDD_tube_seal_rack',
        ),
        migrations.RemoveField(
            model_name='calibration_stand',
            name='calibration_orifice_set',
        ),
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='TTD_tube_seal_rack',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='pressure_senser',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='supply_orifice_set',
        ),
        migrations.DeleteModel(
            name='BDD',
        ),
        migrations.DeleteModel(
            name='BDD_tube_seal_rack',
        ),
        migrations.DeleteModel(
            name='Calibration_orifice',
        ),
        migrations.DeleteModel(
            name='CALIBRATION_STAND',
        ),
        migrations.DeleteModel(
            name='Pressure_senser',
        ),
        migrations.DeleteModel(
            name='Supply_orifice',
        ),
        migrations.DeleteModel(
            name='TTD',
        ),
        migrations.DeleteModel(
            name='TTD_tube_seal_rack',
        ),
    ]