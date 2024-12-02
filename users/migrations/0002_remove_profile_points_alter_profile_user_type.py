# Generated by Django 5.1.2 on 2024-11-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="points",
        ),
        migrations.AlterField(
            model_name="profile",
            name="user_type",
            field=models.CharField(
                blank=True, default="Standard", max_length=255, null=True
            ),
        ),
    ]
