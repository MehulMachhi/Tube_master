# Generated by Django 4.1.1 on 2022-10-07 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0076_remove_plant_client_remove_reactor_unit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='name_of_the_unit',
            new_name='name_of_unit',
        ),
    ]
