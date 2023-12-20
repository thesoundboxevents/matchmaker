from django.shortcuts import render

def dashboard(request):
    return render(request, 'musician_dash/dashboard.html')

# Remove the chat_with_gpt view and any other unused imports or functions