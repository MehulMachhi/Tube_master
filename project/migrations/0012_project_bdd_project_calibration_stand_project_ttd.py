# Generated by Django 4.1.1 on 2022-12-02 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0021_alter_bdd_image_alter_calibration_stand_image_and_more'),
        ('project', '0011_alter_project_equipment_delivery_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bdd',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.bdd', verbose_name='BDD'),
        ),
        migrations.AddField(
            model_name='project',
            name='calibration_stand',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.calibration_stand', verbose_name='CALIBRATION_STAND'),
        ),
        migrations.AddField(
            model_name='project',
            name='ttd',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.ttd', verbose_name='TTD'),
        ),
    ]
