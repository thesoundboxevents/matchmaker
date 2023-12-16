# ChatGPT_Integration/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistProfileViewSet

router = DefaultRouter()
router.register(r'artistprofiles', ArtistProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
