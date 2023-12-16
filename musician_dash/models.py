#models.py inside musician_dash

from django.db import models
# Create your models here.

class ArtistAdditionalDetails(models.Model):
    artist_profile = models.OneToOneField('NewUserApp.ArtistProfile', on_delete=models.CASCADE, related_name='additional_details')
    genres = models.ManyToManyField('NewUserApp.Genre')
    artist_address = models.ForeignKey('NewUserApp.ArtistAddress', on_delete=models.SET_NULL, null=True, blank=True)
    experience_years = models.IntegerField(default=0)
    awards = models.TextField(blank=True)
    education = models.TextField(blank=True)
    audio_video_samples = models.JSONField(blank=True, null=True)  # Links to audio/video samples
    photo_gallery = models.JSONField(blank=True, null=True)  # Links to gallery images
    availability_schedule = models.JSONField(blank=True, null=True)  # JSON structure for availability
    preferred_venues = models.TextField(blank=True)
    travel_willingness = models.BooleanField(default=False)
    equipment_needs = models.TextField(blank=True)
    technical_rider = models.TextField(blank=True)
    rate_information = models.TextField(blank=True)
    payment_preferences = models.TextField(blank=True)
    covid_vaccination_status = models.BooleanField(default=False)
    dietary_preferences = models.TextField(blank=True)
    insurance_details = models.TextField(blank=True)
    contractual_preferences = models.TextField(blank=True)
    languages_spoken = models.CharField(max_length=256, blank=True)
    personal_interests = models.TextField(blank=True)