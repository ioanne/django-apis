from django.contrib import admin

from api.v1.inventory.models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("character", "item", "quantity", "equipped")
    list_filter = ("character", "item", "equipped")
    search_fields = ("character", "item", "equipped")
