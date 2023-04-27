# Generated by Django 4.1.1 on 2023-01-27 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("part", "0021_part_alternate_name_part_asset_number_and_more"),
        (
            "client",
            "0116_alter_client_alternate_name_alter_client_comman_name_and_more",
        ),
        ("project", "0017_scope_of_work_project_equipment_info_remarks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="part",
            field=models.ForeignKey(
                blank=True,
                default="",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="part.part",
            ),
        ),
        migrations.RemoveField(
            model_name="project",
            name="reactor",
        ),
        migrations.AddField(
            model_name="project",
            name="reactor",
            field=models.ManyToManyField(
                to="client.reactor", verbose_name="Reactor Name"
            ),
        ),
    ]