# YourProjectName/urls.py (e.g., Matchmaker/urls.py)

from django.contrib import admin
from django.urls import path, include
from HomePageApp.views import home_view  # Importing the home_view from HomePageApp
from Musician_Dash import views
#profiles/home/admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # URL pattern for the home page
    path('dashboard/', views.dashboard, name='musician_dashboard'),
    path('venue-dash/', include('Venue_Dash.urls')),
    path('new_user/', include('NewUserApp.urls')),  # Corrected
    path('api/', include('ChatGPT_Integration.urls')),
    path('musician_dash/', include('Musician_Dash.urls')),
    path('data_cleaner/', include('Data_Cleaner_and_Handler.urls')),

]

