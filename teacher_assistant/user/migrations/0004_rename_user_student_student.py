# Generated by Django 5.0.6 on 2024-07-22 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_rename_user_teacher_teacher"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="user",
            new_name="student",
        ),
    ]
