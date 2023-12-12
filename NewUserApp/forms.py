from django import forms
from .models import ArtistProfile
from .models import ArtistAddress

class ArtistSignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150)  # For creating User instance
    email = forms.EmailField(max_length=280)  # Email field

    class Meta:
        model = ArtistProfile
        fields = ['username', 'first_name', 'last_name', 'stage_name', 'date_of_birth', 'phone_number', 'instagram_handle', 'facebook_link', 'email']

class ArtistAddressForm(forms.ModelForm):
    class Meta:
        model = ArtistAddress
        fields = ['line1', 'line2', 'town_or_city', 'county', 'postcode', 'country']

