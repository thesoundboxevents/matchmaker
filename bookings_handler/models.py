from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to User model in another app
    venue_id = models.IntegerField()  #venue details are managed 
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')])
    special_requests = models.TextField(blank=True)
    number_of_attendees = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking at Venue ID {self.venue_id} by User ID {self.user_id} on {self.start_time}"
