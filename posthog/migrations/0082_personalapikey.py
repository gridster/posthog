# Generated by Django 3.0.6 on 2020-07-29 09:02

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import posthog.models.utils


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0081_person_is_identified"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalAPIKey",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=posthog.models.utils.generate_random_token,
                        max_length=50,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("label", models.CharField(max_length=40)),
                (
                    "value",
                    models.CharField(
                        default=posthog.models.utils.generate_random_token,
                        editable=False,
                        max_length=50,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("last_used_at", models.DateTimeField(blank=True, null=True)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="personal_api_keys",
                        to="posthog.Team",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="personal_api_keys",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
