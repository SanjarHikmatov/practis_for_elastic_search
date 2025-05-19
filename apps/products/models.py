from django.db import models


class Product(models.Model):
    title =models.TextField(max_length=10000, blank=True,null=True)
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

