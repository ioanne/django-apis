from rest_framework import generics

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.v1.character.models import Character
from api.v1.character.serializers import CharacterSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class CharacterListCreateView(generics.ListCreateAPIView):  # characters/ GET POST
    # queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(user=user)


# characters/1/ GET PUT DELETE
class CharacterRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
