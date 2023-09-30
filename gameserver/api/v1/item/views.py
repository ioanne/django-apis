from rest_framework import generics

from api.v1.item.models import Item
from api.v1.item.serializers import ItemSerializer


# items/ GET POST
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# items/1/ GET PUT DELETE
class ItemRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
