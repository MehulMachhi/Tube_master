# Generated by Django 4.1.1 on 2022-12-07 08:01

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0094_alter_unit_plant'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='country',
            field=smart_selects.db_fields.GroupedForeignKey(default='', group_field='client', on_delete=django.db.models.deletion.CASCADE, related_name='countryplant', to='client.plant'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='plant',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='client', chained_model_field='official_name', null=True, on_delete=django.db.models.deletion.CASCADE, show_all=True, to='client.plant'),
        ),
    ]