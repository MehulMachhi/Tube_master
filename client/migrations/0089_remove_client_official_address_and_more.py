# Generated by Django 4.1.1 on 2022-11-11 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0088_remove_client_official_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='official_address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='plantentrance_address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='shipping_address',
        ),
        migrations.AddField(
            model_name='client',
            name='official_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='official_address', to='client.address'),
        ),
        migrations.AddField(
            model_name='client',
            name='plantentrance_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plantentrance_address', to='client.address'),
        ),
        migrations.AddField(
            model_name='client',
            name='shipping_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='client.address'),
        ),
    ]