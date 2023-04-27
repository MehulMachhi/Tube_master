# Generated by Django 3.2.16 on 2023-03-14 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0032_alter_bdd_tube_seal_rack_number_of_tubes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='alternate_name',
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
            name='part_function',
        ),
        migrations.RemoveField(
            model_name='part',
            name='part_no',
        ),
        migrations.AddField(
            model_name='part',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='name_of_abbreviation',
            field=models.CharField(blank=True, max_length=128, verbose_name='Abbreviation'),
        ),
    ]