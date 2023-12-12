# In Matchmaker/NewUserApp/views.py

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .forms import ArtistSignupForm, ArtistAddressForm
import logging
from django.shortcuts import render, redirect
from .models import ArtistProfile
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def success(request):
    # Your success view logic here
    return render(request, 'NewUserApp/success.html')

def user_type_selection(request):
    # Logic for the user_type_selection view
    return render(request, 'NewUserApp/user_type_selection.html')

def venue_signup(request):
    # Logic for the venue_signup view
    return render(request, 'NewUserApp/venue_signup.html')


logger = logging.getLogger(__name__)

def artist_signup(request):
    if request.method == 'POST':
        signup_form = ArtistSignupForm(request.POST)
        address_form = ArtistAddressForm(request.POST)

        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        if password != password_confirm:
            messages.error(request, "Passwords do not match")
            return render(request, 'NewUserApp/artist_signup.html', {'signup_form': signup_form, 'address_form': address_form})

        if signup_form.is_valid() and address_form.is_valid():
            user = User(
                username=signup_form.cleaned_data['username'],
                email=signup_form.cleaned_data['email'],
                password=make_password(password),
            )
            user.save()

            artist_profile = ArtistProfile(
                user=user,
                first_name=signup_form.cleaned_data.get('first_name', ''),
                last_name=signup_form.cleaned_data.get('last_name', ''),
                stage_name=signup_form.cleaned_data.get('stage_name', ''),
                date_of_birth=signup_form.cleaned_data.get('date_of_birth'),
                phone_number=signup_form.cleaned_data.get('phone_number', ''),
                instagram_handle=signup_form.cleaned_data.get('instagram_handle', ''),
                facebook_link=signup_form.cleaned_data.get('facebook_link', ''),
                email=signup_form.cleaned_data.get('email', ''),
            )
            artist_profile.save()
            # ... rest of your code ...


            logger.info("Artist signup form saved successfully.")
            return redirect('success_url')
        else:
            messages.error(request, "Form is not valid")
            logger.warning("Artist signup form validation failed.")
    else:
        signup_form = ArtistSignupForm()
        address_form = ArtistAddressForm()

    return render(request, 'NewUserApp/artist_signup.html', {'signup_form': signup_form, 'address_form': address_form})


