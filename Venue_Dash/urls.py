#urls.py inside venues_dash

# venues_dash/urls.py
from django.urls import path
from .views import venue_dashboard

urlpatterns = [
    path('dashboard/', venue_dashboard, name='venue_dashboard'),
]
