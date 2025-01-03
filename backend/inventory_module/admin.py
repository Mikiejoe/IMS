from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ["sku", "item", "category", "quantity", "supplier"]
    search_fields = ["item"]
    list_filter = ["item", "category", "supplier"]
    preserve_filters = True
    # search_help_text = "enter item name?"
    list_select_related = True


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.InventoryItem, InventoryItemAdmin)
