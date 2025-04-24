from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Store(models.Model):
    PLATFORM_CHOICES = [
        ('woocommerce', 'WooCommerce'),
        ('shopify', 'Shopify'),
    ]

    company = models.ForeignKey(Company, related_name='stores', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    domain = models.URLField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.platform})"