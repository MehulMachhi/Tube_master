# Generated by Django 3.2.16 on 2023-02-07 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0024_auto_20230207_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bdd_tube_seal_rack',
            options={'verbose_name': 'BDD Tube Seal Rack'},
        ),
        migrations.AlterModelOptions(
            name='calibration_orifice',
            options={'verbose_name': 'Calibration Orifice'},
        ),
        migrations.AlterModelOptions(
            name='devicehose',
            options={'verbose_name': 'Device Hose'},
        ),
        migrations.AlterModelOptions(
            name='supply_orifice',
            options={'verbose_name': 'Supply Orifice'},
        ),
        migrations.AlterModelOptions(
            name='swabmastertsr',
            options={'verbose_name': 'SwabMaster Tube Seal Rack'},
        ),
        migrations.AlterModelOptions(
            name='ttd_tube_seal_rack',
            options={'verbose_name': 'TDD Tube Seal Rack'},
        ),
    ]