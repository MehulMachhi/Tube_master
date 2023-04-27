# Generated by Django 4.1.1 on 2023-01-18 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0017_remove_part_part_abbreviation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='PM_STATUS',
        ),
        migrations.RemoveField(
            model_name='part',
            name='is_this_part_of_set',
        ),
        migrations.RemoveField(
            model_name='part',
            name='it_is_an_assembly',
        ),
        migrations.RemoveField(
            model_name='part',
            name='packaging',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_alternate_name',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_asset_number',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_location_of_storage',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_serial_number',
        ),
        migrations.AddField(
            model_name='part',
            name='part_function',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='part_no',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_name',
            field=models.CharField(blank=True, default=1, max_length=128),
            preserve_default=False,
        ),
    ]