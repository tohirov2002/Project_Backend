# Generated by Django 5.0.6 on 2024-05-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentsmodel",
            name="description_ru",
            field=models.TextField(default=1),
        ),
    ]
