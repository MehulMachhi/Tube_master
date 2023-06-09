# Generated by Django 4.1.1 on 2023-01-30 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0018_project_part_remove_project_reactor_project_reactor"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                limit_choices_to={"is_active": True},
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
