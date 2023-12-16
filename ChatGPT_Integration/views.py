# In views.py
from rest_framework.decorators import action
from rest_framework import viewsets, status
from NewUserApp.models import ArtistProfile
from NewUserApp.serializers import ArtistProfileSerializer
from rest_framework.response import Response
from .chatgpt_client import ChatGPTClient

class ArtistProfileViewSet(viewsets.ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer

    @action(detail=False, methods=['post'])
    def chat(self, request):
        user_profile = self.get_queryset().first()
        chat_client = ChatGPTClient()
        prompt = request.data.get('prompt')
        if not prompt:
            return Response({"error": "Prompt is required."}, status=status.HTTP_400_BAD_REQUEST)
        personalized_prompt = f"{user_profile.stage_name}: {prompt}"
        response = chat_client.get_response(personalized_prompt)
        return Response(response, status=status.HTTP_200_OK)

# In urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArtistProfileViewSet

router = DefaultRouter()
router.register(r'artistprofiles', ArtistProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
