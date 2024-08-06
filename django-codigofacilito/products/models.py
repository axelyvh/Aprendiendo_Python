from django.utils import timezone
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    image = models.ImageField(upload_to='media/products', blank=True, null=True)

    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} | {self.brand}'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name