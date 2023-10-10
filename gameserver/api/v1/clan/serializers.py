from rest_framework import serializers


class ClanInviteSerializer(serializers.Serializer):
    """Serializer para invitar a un usuario a un clan"""

    user_id = serializers.IntegerField()
    leader_id = serializers.IntegerField()
