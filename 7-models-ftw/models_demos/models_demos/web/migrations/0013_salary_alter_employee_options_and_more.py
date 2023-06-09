# Generated by Django 4.2.1 on 2023-06-01 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0012_remove_profile_id_alter_profile_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="Salary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name_plural": "Salaries",
            },
        ),
        migrations.AlterModelOptions(
            name="employee",
            options={"ordering": ["-first_name"]},
        ),
        migrations.RemoveField(
            model_name="employee",
            name="created_on",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="updated_on",
        ),
        migrations.AddField(
            model_name="department",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="department",
            name="updated_on",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="project",
            name="size",
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
