# Generated by Django 5.1.4 on 2024-12-17 12:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="labels",
            old_name="label_name",
            new_name="name",
        ),
    ]
