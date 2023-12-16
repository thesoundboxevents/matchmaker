# NewUserApp/serializers.py

from rest_framework import serializers
from .models import ArtistProfile

class ArtistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile
        fields = ['user', 'first_name', 'last_name', 'stage_name', 'date_of_birth', 'phone_number', 'instagram_handle', 'facebook_link', 'email']
