#views.py inside musician_dash

from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Dashboard view placeholder.")

