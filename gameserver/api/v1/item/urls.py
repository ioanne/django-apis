from django.urls import path
from api.v1.item.views import ItemListCreateView, ItemRetreiveUpdateDestroyView


urlpatterns = [
    path("", ItemListCreateView.as_view(), name="item-list-create"),
    path(
        "<int:pk>/",
        ItemRetreiveUpdateDestroyView.as_view(),
        name="item-retrieve-update-destroy",
    ),
]
