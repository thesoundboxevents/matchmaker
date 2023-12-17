from django.urls import path
from .views import send_to_chatgpt

urlpatterns = [
    path('send-to-chatgpt/', send_to_chatgpt, name='send_to_chatgpt'),
]