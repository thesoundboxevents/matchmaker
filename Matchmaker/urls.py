# YourProjectName/urls.py (e.g., Matchmaker/urls.py)

from django.contrib import admin
from django.urls import path, include
from HomePageApp.views import home_view  # Importing the home_view from HomePageApp

#profiles/home/admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # URL pattern for the home page
    path('musician_dash/', include('Musician_Dash.urls')),
    path('venue-dash/', include('Venue_Dash.urls')),
    path('new_user/', include('NewUserApp.urls')),  # Corrected

]