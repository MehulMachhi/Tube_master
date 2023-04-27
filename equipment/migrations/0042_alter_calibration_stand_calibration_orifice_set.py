# Generated by Django 3.2.16 on 2023-02-10 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0029_devicehose_length'),
        ('equipment', '0041_auto_20230209_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibration_stand',
            name='calibration_orifice_set',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calibration', to='part.calibration_orifice', verbose_name='Calibration Orifice Set'),
        ),
    ]
