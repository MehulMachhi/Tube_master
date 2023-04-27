# Generated by Django 4.1.1 on 2022-12-07 07:26

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0092_remove_reactor_tube_material_of_rows_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='plant',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='client', chained_model_field='client', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='client.plant'),
        ),
    ]
