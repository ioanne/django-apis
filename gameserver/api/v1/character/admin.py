from django.contrib import admin

from api.v1.character.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "nivel", "banned", "blocked", "user")
    search_fields = ("name", "user__username")
    list_filter = ("banned", "blocked")
