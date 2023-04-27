# Generated by Django 4.1.1 on 2022-10-10 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0078_remove_client_plant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='name_of_unit',
        ),
        migrations.AddField(
            model_name='plant',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Client Plant+', to='client.client'),
        ),
    ]
