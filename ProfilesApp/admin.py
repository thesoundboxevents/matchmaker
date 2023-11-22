from django.contrib import admin
from .models import Profile

from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_musician', 'is_venue_manager', 'phone_number']
    list_filter = ['is_musician', 'is_venue_manager', 'user__is_active']
    search_fields = ['user__username', 'user__email', 'phone_number']
    readonly_fields = ['user']

