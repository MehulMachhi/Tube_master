# Generated by Django 4.1.1 on 2022-09-22 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0033_rename_no_of_unit_plant_name_of_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='plant',
        ),
        migrations.AddField(
            model_name='client',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.plant'),
        ),
    ]
