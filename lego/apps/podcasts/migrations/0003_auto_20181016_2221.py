# Generated by Django 2.0.6 on 2018-10-16 22:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("podcasts", "0002_podcast_authors"),
    ]

    operations = [
        migrations.AddField(
            model_name="podcast",
            name="thanks",
            field=models.ManyToManyField(
                blank=True, related_name="thanks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="podcast",
            name="authors",
            field=models.ManyToManyField(
                blank=True, related_name="authors", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]