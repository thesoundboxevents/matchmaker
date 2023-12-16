#views.py inside musician_dash

from django.shortcuts import render

def dashboard(request):
    return render(request, 'musician_dash/dashboard.html')


