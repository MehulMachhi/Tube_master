# Generated by Django 4.1.1 on 2022-12-12 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0005_remove_bdd_bdd_tube_seal_rack_and_more'),
        ('part', '0011_remove_part_part_image'),
        ('equipment', '0024_alter_bdd_location_for_warehouse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='BDD_tube_seal_rack',
            field=models.ManyToManyField(to='part.bdd_tube_seal_rack', verbose_name='BDD Tube Seal Rack'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Alternate Name'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='asset_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Asset Number'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='if_yes_how_many_in_a_set',
            field=models.CharField(blank=True, max_length=128, verbose_name='If Yes How Many In A Set?'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='is_this_part_of_set',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, verbose_name='Is This Part Of Set?'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='location_for_storage',
            field=models.CharField(blank=True, max_length=128, verbose_name='Location For Storage'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='pm_status',
            field=models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, verbose_name='PM Status'),
        ),
        migrations.AlterField(
            model_name='bdd',
            name='serial_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Alternate Name'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='asset_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Asset Number'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='cal_stand_size',
            field=models.CharField(blank=True, max_length=128, verbose_name='Calibration Stand Size'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='calibration_orifice_set',
            field=models.ManyToManyField(to='part.calibration_orifice', verbose_name='Calibration Orifice Set'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='if_yes_how_many_in_a_set',
            field=models.CharField(blank=True, max_length=128, verbose_name='If Yes How Many In A Set?'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='is_this_part_of_set',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, verbose_name='Is This Part Of Set?'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='location_for_storage',
            field=models.CharField(blank=True, max_length=128, verbose_name='Location For Storage'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='pm_status',
            field=models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, verbose_name='PM Status'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='serial_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='TTD_tube_seal_rack',
            field=models.ManyToManyField(to='part.ttd_tube_seal_rack', verbose_name='TTD Tube Seal Rack'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Alternate Name'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='asset_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Asset Number'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='if_yes_how_many_in_a_set',
            field=models.CharField(blank=True, max_length=128, verbose_name='If Yes How Many In A Set?'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='is_this_part_of_set',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=128, verbose_name='Is This Part Of Set'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='location_for_storage',
            field=models.CharField(blank=True, max_length=128, verbose_name='Location For Storage'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='pm_status',
            field=models.CharField(choices=[('RED', 'RED'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN')], max_length=20, verbose_name='PM Status'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='pressure_sensor',
            field=models.ManyToManyField(to='part.pressure_sensor', verbose_name='Pressure Sensor'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='serial_number',
            field=models.CharField(blank=True, max_length=128, verbose_name='Serial Number'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='supply_orifice_set',
            field=models.ManyToManyField(to='part.supply_orifice', verbose_name='Supply Orifice Set'),
        ),
    ]
