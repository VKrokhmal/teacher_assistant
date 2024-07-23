# Generated by Django 5.0.6 on 2024-07-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_rename_student_student_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="teachers",
            field=models.ManyToManyField(related_name="students", to="user.teacher"),
        ),
    ]
