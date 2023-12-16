# ChatGPT_Integration/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from .chatgpt_client import ChatGPTClient
from django.contrib.auth.models import User
from NewUserApp.models import ArtistProfile  # Import the ArtistProfile model
from NewUserApp.serializers import ArtistProfileSerializer  # Import the ArtistProfileSerializer

class ChatGPTIntegrationTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        # Create an ArtistProfile instance for the test user
        self.artist_profile = ArtistProfile.objects.create(user=self.user, stage_name="Test Artist")
        self.client.force_authenticate(user=self.user)

    @patch.object(ChatGPTClient, 'get_response')
    def test_chat_endpoint(self, mock_get_response):
        mock_get_response.return_value = {'choices': [{'text': 'Mock response from ChatGPT'}]}
        response = self.client.post(reverse('chat-gpt'), {'prompt': 'Hello ChatGPT'}, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Mock response from ChatGPT', response.data['choices'][0]['text'])

    # Add more tests as needed to cover various scenarios and edge cases
