# Generated by Django 4.1.1 on 2022-11-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0020_alter_bdd_image_alter_calibration_stand_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdd',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='uploads/bdd/'),
        ),
        migrations.AlterField(
            model_name='calibration_stand',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='uploads/cal_stand/'),
        ),
        migrations.AlterField(
            model_name='ttd',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='uploads/ttd/'),
        ),
    ]
