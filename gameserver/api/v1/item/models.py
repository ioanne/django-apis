from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stackable = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.id}) - {self.description} - {self.stackable}"
