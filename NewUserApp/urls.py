from django.urls import path
from . import views
from django.urls import path
from .views import artist_signup
from .views import success

urlpatterns = [
    path('select_user_type/', views.user_type_selection, name='user_type_selection'),
    path('venue_signup/', views.venue_signup, name='venue_signup'),
    path('artist_signup/', artist_signup, name='artist_signup'),
    path('success/', success, name='success_url'),
    # Add other necessary URL patterns
]
