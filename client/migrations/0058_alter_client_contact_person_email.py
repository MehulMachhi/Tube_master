# Generated by Django 4.1.1 on 2022-10-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0057_client_contact_person_client_contact_person_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='contact_person_email',
            field=models.EmailField(blank=True, max_length=128),
        ),
    ]