import json
from rest_framework import serializers

from api.v1.inventory.models import Inventory
from api.v1.character.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "name", "nivel", "title")


class InventorySerializer(serializers.ModelSerializer):
    character = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = "__all__"

    def get_character(self, instance):
        return CharacterSerializer(instance.character).data
