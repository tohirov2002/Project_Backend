# Generated by Django 5.0.6 on 2024-05-13 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_department", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="department",
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
            },
        ),
        migrations.RemoveField(
            model_name="department",
            name="category",
        ),
        migrations.RemoveField(
            model_name="department",
            name="description1",
        ),
        migrations.RemoveField(
            model_name="department",
            name="description2",
        ),
        migrations.RemoveField(
            model_name="department",
            name="description3",
        ),
        migrations.RemoveField(
            model_name="department",
            name="name",
        ),
        migrations.RemoveField(
            model_name="department",
            name="name_cafedra",
        ),
        migrations.RemoveField(
            model_name="departmentcategory",
            name="category_name",
        ),
        migrations.AddField(
            model_name="department",
            name="category_ru",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departments_ru",
                to="app_department.departmentcategory",
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="category_uz",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departments_uz",
                to="app_department.departmentcategory",
            ),
        ),
        migrations.AddField(
            model_name="department",
            name="description1_ru",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="description1_uz",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="description2_ru",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="description2_uz",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="description3_ru",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="description3_uz",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="name_cafedra_ru",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="name_cafedra_uz",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="name_ru",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="department",
            name="name_uz",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="departmentcategory",
            name="category_name_ru",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="departmentcategory",
            name="category_name_uz",
            field=models.CharField(default=1, max_length=255),
        ),
    ]