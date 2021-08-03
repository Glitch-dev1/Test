from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length = 50)
    price       = models.DecimalField(
        max_digits = 10000,
        decimal_places = 2,
        null = True
        )
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    def get_object_url(self):
        return f"/product/{self.id}/"