from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    #add any aditional logic her
    return render(request, 'musician_dash/dashboard.html')

