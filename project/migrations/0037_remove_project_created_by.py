# Generated by Django 3.2.16 on 2023-04-25 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0036_alter_project_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]
