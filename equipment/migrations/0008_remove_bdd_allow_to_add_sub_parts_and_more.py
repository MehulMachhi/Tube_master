# Generated by Django 4.1.1 on 2022-10-19 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_remove_bdd_is_it_an_assembly_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bdd',
            name='allow_to_add_sub_parts',
        ),
        migrations.RemoveField(
            model_name='calibration_stand',
            name='allow_to_add_sub_parts',
        ),
        migrations.RemoveField(
            model_name='ttd',
            name='allow_to_add_sub_parts',
        ),
    ]