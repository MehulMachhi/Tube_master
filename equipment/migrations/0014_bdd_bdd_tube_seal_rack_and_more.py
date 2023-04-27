# Generated by Django 4.1.1 on 2022-10-20 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0001_initial'),
        ('tube', '0005_remove_bdd_bdd_tube_seal_rack_and_more'),
        ('equipment', '0013_remove_ttd_location_for_warehouse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bdd',
            name='BDD_tube_seal_rack',
            field=models.ManyToManyField(to='part.bdd_tube_seal_rack'),
        ),
        migrations.AddField(
            model_name='calibration_stand',
            name='cal_stand_size',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='calibration_stand',
            name='calibration_orifice_set',
            field=models.ManyToManyField(to='part.calibration_orifice'),
        ),
        migrations.RemoveField(
            model_name='bdd',
            name='location_for_warehouse',
        ),
        migrations.RemoveField(
            model_name='calibration_stand',
            name='location_for_warehouse',
        ),
        migrations.AddField(
            model_name='bdd',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Warehouse Location'),
        ),
        migrations.AddField(
            model_name='calibration_stand',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Warehouse Location'),
        ),
    ]