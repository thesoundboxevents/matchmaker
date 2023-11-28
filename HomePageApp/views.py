#views.py inside HomePageApp

from django.shortcuts import render

# HomePageApp/views.py

from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

