# Generated by Django 4.1.1 on 2022-12-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_project_bdd_alter_project_calibration_stand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='contract',
            field=models.CharField(choices=[('DIRECT', 'DIRECT'), ('SUB', 'SUB')], default='', max_length=128, verbose_name='Contract'),
        ),
        migrations.AlterField(
            model_name='project',
            name='scope_of_work',
            field=models.CharField(choices=[('PD_TESTING', 'PD_TESTING'), ('BD', 'BD'), ('TC', 'TC'), ('JAC', 'JAC'), ('OLE', 'OLE'), ('FULL_TURN_KEY', 'FULL_TURN_KEY'), ('OTHER', 'OTHER')], default='', max_length=128, verbose_name='Scope Of Work'),
        ),
    ]