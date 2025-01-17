# Generated by Django 3.2.12 on 2022-02-24 11:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0022_alter_semesterstatus_contacted_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="semesterstatus",
            name="contacted_status",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("company_presentation", "company_presentation"),
                        ("course", "course"),
                        ("lunch_presentation", "lunch_presentation"),
                        ("bedex", "bedex"),
                        ("contact_in_oslo", "contact_in_oslo"),
                        ("interested", "interested"),
                        ("not_interested", "not_interested"),
                        ("contacted", "contacted"),
                        ("not_contacted", "not_contacted"),
                    ],
                    max_length=64,
                ),
                blank=True,
                null=True,
                size=None,
            ),
        ),
    ]
