from django.shortcuts import render
from .models import VenueProfile

def venue_list(request):
    venues = VenueProfile.objects.all()
    # Note the capital 'P' in 'venue_Profiles'
    return render(request, 'venue_Profiles/venue_list.html', {'venues': venues})

