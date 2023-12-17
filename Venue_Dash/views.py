#views.py inside venues_dash

# venues_dash/views.py
from django.shortcuts import render
from django.http import JsonResponse
from ChatGPT_Integration.chatgpt_client import ChatGPTClient


def venue_dashboard(request):
    return render(request, 'venue_dash/dashboard.html')

from django.http import JsonResponse
from ChatGPT_Integration.chatgpt_client import ChatGPTClient
