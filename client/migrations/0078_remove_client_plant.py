# Generated by Django 4.1.1 on 2022-10-10 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0077_rename_name_of_the_unit_unit_name_of_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='plant',
        ),
    ]
