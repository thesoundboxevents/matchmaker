from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profile(models.Model):
    # Linking to Django's User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Bio and profile picture
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # Role identification
    is_musician = models.BooleanField(default=False)
    is_venue_manager = models.BooleanField(default=False)

    # Contact information
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # Identification document upload
    id_document = models.FileField(upload_to='id_documents/', blank=True, null=True, help_text="Upload identification documents here.")

    # Address fields
    street_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state_province = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"



