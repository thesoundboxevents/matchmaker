from django.contrib import admin
from .models import ArtistProfile

@admin.register(ArtistProfile)
class ArtistProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'stage_name', 'date_of_birth',)  # 'email' removed
