from django.shortcuts import render

def user_type_selection(request):
    # Updated to reference NewUserApp instead of AuthenticationApp
    return render(request, 'NewUserApp/user_type_selection.html')

def artist_signup(request):
    # Logic for handling artist signup
    # Updated to reference NewUserApp instead of AuthenticationApp
    return render(request, 'NewUserApp/artist_signup.html')

def venue_signup(request):
    # Logic for handling venue signup
    # Updated to reference NewUserApp instead of AuthenticationApp
    return render(request, 'NewUserApp/venue_signup.html')
