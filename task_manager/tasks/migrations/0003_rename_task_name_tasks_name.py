# Generated by Django 5.1.4 on 2024-12-17 12:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tasks",
            old_name="task_name",
            new_name="name",
        ),
    ]