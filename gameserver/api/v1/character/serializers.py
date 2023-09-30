from rest_framework import serializers

from api.v1.character.models import Character
from api.v1.inventory.serializers import InventorySerializer


class CharacterSerializer(serializers.ModelSerializer):
    inventory = InventorySerializer(source="inventory_set", many=True, read_only=True)
    character_info = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = "__all__"

    def get_character_info(self, instance):
        """Campo calculado del serializer"""
        return f"{instance.name} {instance.nivel} {instance.title}"
