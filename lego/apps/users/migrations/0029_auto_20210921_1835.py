# Generated by Django 2.2.24 on 2021-09-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0028_auto_20210523_1252"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="allergies",
            field=models.CharField(
                blank=True, max_length=500, verbose_name="allergies"
            ),
        ),
    ]
