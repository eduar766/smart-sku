from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'store', 'source_type', 'published', 'created_at')
    list_filter = ('source_type', 'published', 'company', 'store')
    search_fields = ('title',)