from django.contrib import admin
from .models import Company, Store

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'platform', 'company', 'active', 'created_at')
    list_filter = ('platform', 'active')
    search_fields = ('name', 'company__name')