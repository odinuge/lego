# Generated by Django 2.1.11 on 2020-02-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0021_auto_20190829_1632")]

    operations = [
        migrations.AddField(
            model_name="user",
            name="selected_theme",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="selected theme"
            ),
        )
    ]
