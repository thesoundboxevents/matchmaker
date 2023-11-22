# ProfilesApp/urls.py

from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('login/', CustomLoginView.as_view(), name='login'),

    # ... other url patterns specific to ProfilesApp ...
]
