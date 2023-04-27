# Generated by Django 4.1.1 on 2022-12-08 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0005_remove_bdd_bdd_tube_seal_rack_and_more'),
        ('equipment', '0022_alter_bdd_is_this_part_of_set_alter_bdd_pm_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Warehouse Location'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Warehouse Location'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='location_for_warehouse',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Warehouse Location'),
        ),
    ]