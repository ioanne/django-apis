from django.urls import path

from api.v1.clan.views import ClanInviteCreateAPIView


urlpatterns = [
    path("invite/", ClanInviteCreateAPIView.as_view(), name="invite"),
]
