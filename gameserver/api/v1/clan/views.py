from django.http import HttpResponse
from api.v1.character.models import Character

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView

from api.v1.clan.serializers import ClanInviteSerializer
from api.v1.clan.models import Clan, ClanMember


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ClanInviteCreateAPIView(CreateAPIView):
    queryset = Character.objects.all()
    serializer_class = ClanInviteSerializer

    def create(self, request, *args, **kwargs):
        print(kwargs)
        user_to_invite = request.data["user_id"]
        leader = request.user.characters.filter(id=request.data["leader_id"]).last()
        clan = Clan.objects.filter(leader=leader).last()  # Authorizacion
        if clan:
            clan_member = ClanMember.objects.filter(character_id=user_to_invite)
            if not clan_member:
                ClanMember.objects.create(clan=clan, character_id=user_to_invite)
                return HttpResponse("Se ha invitado al clan.", status=201)
            else:
                return HttpResponse("El usuario ya es miembro del clan.", status=200)
        return HttpResponse("Unauthorized", status=401)
