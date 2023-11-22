from django.shortcuts import render, redirect  # Combine imports into one line
from .forms import UserRegistrationForm, ProfileForm  # Combine form imports into one line
from django.contrib.auth.decorators import login_required


# Registration View
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile  # Import your Profile model

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save User
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # Save Profile
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user  # Associate the user with the profile
            new_profile.save()

            return redirect('login')  # Redirect to login after successful registration
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()  # Initialize an empty profile form

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profiles/register.html', context)


# Profile Creation/Editing View
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')  # Redirect after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

# ProfilesApp/views.py
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'profiles/login.html'
    # You can add additional context or methods if needed


@login_required
def post_login_redirect(request):
    if request.user.profile.is_musician:  # Assumption: user has a one-to-one link to profile
        return redirect('/musician_dash/dashboard/')
    else:
        return redirect('/some_other_default_dashboard/')
