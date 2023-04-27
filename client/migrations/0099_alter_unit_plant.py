# Generated by Django 4.1.1 on 2022-12-07 08:45

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0098_alter_unit_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='plant',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='client', chained_model_field='client', on_delete=django.db.models.deletion.CASCADE, to='client.plant'),
        ),
    ]