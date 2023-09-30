from django.urls import path
from api.v1.inventory.views import (
    InventoryListCreateView,
    InventoryRetreiveUpdateDestroyView,
)


urlpatterns = [
    path("", InventoryListCreateView.as_view(), name="inventory-list-create"),
    path(
        "<int:pk>/",
        InventoryRetreiveUpdateDestroyView.as_view(),
        name="inventory-retrieve-update-destroy",
    ),
]
