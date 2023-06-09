# Generated by Django 4.1.1 on 2022-10-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0018_alter_bdd_location_for_warehouse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='image',
            field=models.FileField(default='', upload_to='uploads/bdd/'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='image',
            field=models.FileField(default='', upload_to='uploads/cal_stand/'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='image',
            field=models.FileField(default='', upload_to='uploads/ttd/'),
        ),
    ]
