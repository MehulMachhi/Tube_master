# Generated by Django 4.1.1 on 2022-10-14 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0086_address_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='client',
        ),
    ]
