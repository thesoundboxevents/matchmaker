# Generated by Django 4.2.7 on 2023-11-21 13:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bio", models.TextField(blank=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, null=True, upload_to="profiles/"),
                ),
                ("is_musician", models.BooleanField(default=False)),
                ("is_venue_manager", models.BooleanField(default=False)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                (
                    "id_document",
                    models.FileField(
                        blank=True,
                        help_text="Upload identification documents here.",
                        null=True,
                        upload_to="id_documents/",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "Profile", "verbose_name_plural": "Profiles",},
        ),
    ]
