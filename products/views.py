from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(company=self.request.user.company)

    def perform_create(self, serializer):
        # asociar automáticamente empresa y tienda
        company = self.request.user.company
        store = self.request.data.get('store')  # debería venir el ID
        serializer.save(company=company, store_id=store)