# venues_dash/views.py
from django.shortcuts import render

def venue_dashboard(request):
    return render(request, 'venue_dash/dashboard.html')
