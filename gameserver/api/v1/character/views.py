from rest_framework import generics

from api.v1.character.models import Character
from api.v1.character.serializers import CharacterSerializer


# characters/ GET POST
class CharacterListCreateView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


# characters/1/ GET PUT DELETE
class CharacterRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
