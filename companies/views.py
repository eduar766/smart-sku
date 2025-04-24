from rest_framework import generics, permissions
from .models import Company, Store
from .serializers import CompanySerializer, StoreSerializer
from accounts.models import User

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        company = serializer.save()
        # asignar empresa al usuario actual si no tiene una
        if self.request.user.company is None:
            self.request.user.company = company
            self.request.user.save()

class StoreListCreateView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # limitar tiendas según la empresa del usuario
        return Store.objects.filter(company=self.request.user.company)

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)