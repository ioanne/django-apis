from django.urls import path
from api.v1.character.views import (
    CharacterListCreateView,
    CharacterRetreiveUpdateDestroyView,
)


urlpatterns = [
    path("", CharacterListCreateView.as_view(), name="character-list-create"),
    path(
        "<int:pk>/",
        CharacterRetreiveUpdateDestroyView.as_view(),
        name="character-retrieve-update-destroy",
    ),
]
