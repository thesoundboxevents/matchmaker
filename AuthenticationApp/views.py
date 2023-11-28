#this is the code for Matchmaker/AuthenticationApp/views.py

from django.shortcuts import render

def user_type_selection(request):
    return render(request, 'AuthenticationApp/user_type_selection.html')

def artist_signup(request):
    # Logic for handling artist signup
    return render(request, 'AuthenticationApp/artist_signup.html')

def venue_signup(request):
    # Logic for handling venue signup
    return render(request, 'AuthenticationApp/venue_signup.html')
