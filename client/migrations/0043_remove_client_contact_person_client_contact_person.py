# Generated by Django 4.1.1 on 2022-09-28 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0042_remove_address_client_remove_contact_client_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='client',
        #     name='contact_person',
        # ),
        # migrations.AddField(
        #     model_name='client',
        #     name='contact_person',
        #     field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Client Contact+', to='client.contact'),
        # ),
    ]
