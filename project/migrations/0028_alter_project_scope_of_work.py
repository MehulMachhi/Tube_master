# Generated by Django 3.2.16 on 2023-03-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_auto_20230228_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='scope_of_work',
            field=models.ManyToManyField(to='project.Scope_of_work', verbose_name='Scope Of Work'),
        ),
    ]
