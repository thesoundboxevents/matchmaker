# Generated by Django 4.2.7 on 2023-12-13 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("NewUserApp", "0003_delete_artistadditionaldetails"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtistAdditionalDetails",
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
                ("experience_years", models.IntegerField(default=0)),
                ("awards", models.TextField(blank=True)),
                ("education", models.TextField(blank=True)),
                ("audio_video_samples", models.JSONField(blank=True, null=True)),
                ("photo_gallery", models.JSONField(blank=True, null=True)),
                ("availability_schedule", models.JSONField(blank=True, null=True)),
                ("preferred_venues", models.TextField(blank=True)),
                ("travel_willingness", models.BooleanField(default=False)),
                ("equipment_needs", models.TextField(blank=True)),
                ("technical_rider", models.TextField(blank=True)),
                ("rate_information", models.TextField(blank=True)),
                ("payment_preferences", models.TextField(blank=True)),
                ("covid_vaccination_status", models.BooleanField(default=False)),
                ("dietary_preferences", models.TextField(blank=True)),
                ("insurance_details", models.TextField(blank=True)),
                ("contractual_preferences", models.TextField(blank=True)),
                ("languages_spoken", models.CharField(blank=True, max_length=256)),
                ("personal_interests", models.TextField(blank=True)),
                (
                    "artist_address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="NewUserApp.artistaddress",
                    ),
                ),
                (
                    "artist_profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="additional_details",
                        to="NewUserApp.artistprofile",
                    ),
                ),
                ("genres", models.ManyToManyField(to="NewUserApp.genre")),
            ],
        ),
    ]
