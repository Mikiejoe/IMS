from django.contrib import admin
from . import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "primary_contact", "secondary_contact"]


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ["email", "phone", "address"]


admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.ContactInfo, ContactInfoAdmin)
