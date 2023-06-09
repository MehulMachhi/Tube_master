# Generated by Django 4.1.1 on 2022-12-08 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0022_alter_bdd_is_this_part_of_set_alter_bdd_pm_status_and_more'),
        ('project', '0014_alter_project_client_alter_project_reactor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='bdd',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='equipment.bdd', verbose_name='BDD'),
        ),
        migrations.AlterField(
            model_name='project',
            name='calibration_stand',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='equipment.calibration_stand', verbose_name='CALIBRATION_STAND'),
        ),
        migrations.AlterField(
            model_name='project',
            name='ttd',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='equipment.ttd', verbose_name='TTD'),
        ),
    ]
