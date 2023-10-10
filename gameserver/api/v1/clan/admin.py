from django.contrib import admin

from api.v1.clan.models import Clan, ClanMember


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("name", "leader")
    search_fields = ("name",)


@admin.register(ClanMember)
class ClanMemberAdmin(admin.ModelAdmin):
    list_display = ("clan", "character")
    search_fields = ("clan__name", "character__name")
    list_filter = ("clan",)
