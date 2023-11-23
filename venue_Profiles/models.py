from django.db import models

class VenueProfile(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    capacity = models.PositiveIntegerField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    # You can add fields like website, genre of music played, etc.

    def __str__(self):
        return self.name


# Create your models here.
