# Generated by Django 4.1.1 on 2022-10-04 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0069_remove_toppingamount_pizza_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='plant',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='name_of_unit',
        ),
        migrations.AddField(
            model_name='plant',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Client Plant+', to='client.client'),
        ),
    ]
