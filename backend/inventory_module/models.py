from django.db import models
from suppliers_module.models import Supplier


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class InventoryItem(models.Model):
    item = models.CharField(max_length=255)
    sku = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    added_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.item
