# Generated by Django 4.1.1 on 2022-09-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0049_alter_client_contact_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='contact_person',
            field=models.ManyToManyField(null=True, related_name='Client Contact+', to='client.contact'),
        ),
    ]
