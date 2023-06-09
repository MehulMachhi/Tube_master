# Generated by Django 3.2.16 on 2023-02-10 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0121_auto_20230210_1116'),
        ('project', '0025_auto_20230210_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='client',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client', verbose_name='Client Name'),
        ),
    ]
