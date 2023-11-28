from django.urls import path
from . import views

urlpatterns = [
    path('select_user_type/', views.user_type_selection, name='user_type_selection'),
    path('artist_signup/', views.artist_signup, name='artist_signup'),
    path('venue_signup/', views.venue_signup, name='venue_signup'),
    # Add other necessary URL patterns
]
