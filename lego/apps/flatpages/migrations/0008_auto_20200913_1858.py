# Generated by Django 2.2.13 on 2020-09-13 18:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20200910_1530'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flatpages', '0007_auto_20200826_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='can_edit_groups',
            field=models.ManyToManyField(blank=True, related_name='can_edit_page', to='users.AbakusGroup'),
        ),
        migrations.AddField(
            model_name='page',
            name='can_edit_users',
            field=models.ManyToManyField(blank=True, related_name='can_edit_page', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='can_view_groups',
            field=models.ManyToManyField(blank=True, related_name='can_view_page', to='users.AbakusGroup'),
        ),
        migrations.AddField(
            model_name='page',
            name='require_auth',
            field=models.BooleanField(default=False),
        ),
    ]
