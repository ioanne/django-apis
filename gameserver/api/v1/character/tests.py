import json
from django.urls import reverse
from rest_framework.test import APITestCase

from api.v1.character.models import Character


class TestCharacter(APITestCase):
    def setUp(self):
        # Mock data
        self.character_data = {
            "name": "Test - 1",
            "nivel": 7,
            "title": "Testing character",
        }
        self.character = Character.objects.create(**self.character_data)

    def test_character_list(self):
        """Test character list"""
        url = reverse("character-list-create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_character_retrieve_update_destroy_view(self):
        url = reverse("character-retrieve-update-destroy", args=[self.character.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], self.character_data["name"])

        put_data = {
            "name": "Test - 1",
            "nivel": 9,
            "title": "Testing character",
        }
        put_response = self.client.put(
            path=url, data=json.dumps(put_data), content_type="application/json"
        )
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response.data["nivel"], put_data["nivel"])

        delete_response = self.client.delete(path=url)
        self.assertEqual(delete_response.status_code, 204)
        self.assertEqual(Character.objects.count(), 0)
