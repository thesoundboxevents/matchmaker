from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models import JSONField

class Genre(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class ArtistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank = True)
    stage_name = models.CharField(max_length=128, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    instagram_handle = models.CharField(max_length=128, blank=True, null=True)  # JSON structure for social media links
    facebook_link = models.CharField(max_length=128, blank=True, null=True)  # JSON structure for social media links
    email = models.EmailField(max_length=254, default = '')
    
    def __str__(self):
        return self.stage_name or self.user.username
    
class ArtistAddress(models.Model):
    line1 = models.CharField(max_length=128, verbose_name='Address Line 1')
    line2 = models.CharField(max_length=128, verbose_name='Address Line 2', blank=True, null=True)
    town_or_city = models.CharField(max_length=64, verbose_name='Town/City')
    county = models.CharField(max_length=64, verbose_name='County')
    postcode = models.CharField(max_length=10, verbose_name='Postcode')
    country = models.CharField(max_length=50, verbose_name='Country', default='United Kingdom')

    def __str__(self):
        address = f"{self.line1}"
        if self.line2:
            address += f", {self.line2}"
        address += f", {self.town_or_city}, {self.county}, {self.postcode}, {self.country}"
        return address


#This is a review model for clients to feedback to the artist & use in machine learning
class Review(models.Model):
    artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Assuming User is the model for reviewers
    title = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.PositiveIntegerField()  # Alternatively, use a DecimalField for more precision
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Specific responses stored in JSON format in database
    questions_responses = JSONField(blank=True, null=True)  # Use a JSONField to store structured question & answer data

    def __str__(self):
        return f"{self.title} by {self.reviewer.username}"


