# Generated by Django 4.2.1 on 2023-06-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0013_salary_alter_employee_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="department",
            name="slug",
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
