# Generated by Django 4.1.1 on 2022-12-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0110_alter_reactor_tube_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactor',
            name='inch',
        ),
        migrations.RemoveField(
            model_name='reactor',
            name='mm',
        ),
        migrations.AddField(
            model_name='reactor',
            name='input_tubeid',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='INCH/MM'),
        ),
    ]
