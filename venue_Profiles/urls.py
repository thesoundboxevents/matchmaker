from django.urls import path
from .views import venue_list

urlpatterns = [
    path('list/', venue_list, name='venue_list'),
]
