"""Matchmaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# YourProjectName/urls.py (e.g., Matchmaker/urls.py)

from django.contrib import admin
from django.urls import path, include
from HomePageApp.views import home_view  # Importing the home_view from HomePageApp

#profiles/home/admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/', include('ProfilesApp.urls')),  # Include URLs from ProfilesApp
    path('', home_view, name='home'),  # URL pattern for the home page
    path('musician_dash/', include('musician_dash.urls')),
    path('venues/', include('venue_Profiles.urls')),
]

#musician dash

