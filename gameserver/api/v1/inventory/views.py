from rest_framework import generics

from api.v1.inventory.models import Inventory
from api.v1.inventory.serializers import InventorySerializer


# inventory/ GET POST
class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# inventories/1/ GET PUT DELETE
class InventoryRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
