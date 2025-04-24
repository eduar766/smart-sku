from rest_framework import serializers
from .models import Company, Store

class StoreSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(read_only=True)  # <- Esto evita que se exija en el input
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Store
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    stores = StoreSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'created_at', 'stores']