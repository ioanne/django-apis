from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User


class CharacterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(banned=False)


class Character(models.Model):
    name = models.CharField(max_length=16)
    title = models.CharField(max_length=25, null=True, blank=True)
    nivel = models.PositiveIntegerField()
    banned = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="characters")

    objects = CharacterManager()
    objects_all = models.Manager()

    def get_clan(self):
        return self.clan_member.first()

    @property
    def member(self):
        return self.clan_member.first()

    @property
    def clan(self):
        clan_member = self.get_clan()
        return clan_member.clan if clan_member else None

    def __str__(self) -> str:
        return f"{self.name}({self.id}) - {self.nivel}"
