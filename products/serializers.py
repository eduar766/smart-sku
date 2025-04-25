from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        read_only_fields = ['company', 'store', 'created_at', 'updated_at', 'published']
        fields = '__all__'