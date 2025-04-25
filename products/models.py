from django.db import models
from companies.models import Company, Store

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products')

    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500, blank=True)
    full_description = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)  # SEO, etiquetas, etc.

    image_url = models.URLField(blank=True)
    source_type = models.CharField(max_length=20, choices=[('image', 'Image'), ('excel', 'Excel')])
    original_file_name = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)  # ¿ya se publicó en Woo o Shopify?

    def __str__(self):
        return self.title