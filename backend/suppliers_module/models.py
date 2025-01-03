from django.db import models


class ContactInfo(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = "supplier contact"
        verbose_name = "supplier contact"


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    primary_contact = models.ForeignKey(
        ContactInfo, on_delete=models.CASCADE, related_name="primary_contact"
    )
    secondary_contact = models.ForeignKey(
        ContactInfo,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="secondary_contact",
    )

    def __str__(self):
        return self.name
