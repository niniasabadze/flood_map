# Generated by Django 5.1.2 on 2024-11-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0008_alter_marker_disruption_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="marker",
            name="raindrop_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]