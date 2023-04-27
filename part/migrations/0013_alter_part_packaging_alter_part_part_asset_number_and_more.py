# Generated by Django 4.1.1 on 2023-01-18 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tube', '0005_remove_bdd_bdd_tube_seal_rack_and_more'),
        ('part', '0012_rename_part_function_part_packaging_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='packaging',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_asset_number',
            field=models.IntegerField(blank=True, max_length=128, verbose_name='Asset Number'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_location_of_storage',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Location For Storage'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_location_of_warehouse',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='tube.warehouse', verbose_name='Location For Warehouse'),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_serial_number',
            field=models.IntegerField(blank=True, max_length=128, verbose_name='Serial Number'),
        ),
    ]
