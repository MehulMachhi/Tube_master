# Generated by Django 4.1.1 on 2022-10-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0072_plant_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='plant',
            field=models.ManyToManyField(related_name='client Plant+', to='client.plant'),
        ),
    ]
