# Generated by Django 4.1.1 on 2022-10-04 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0059_delete_tubeidmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='plant',
            field=models.ManyToManyField(related_name='Client plant+', to='client.plant'),
        ),
    ]