from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
import openpyxl
from .models import Product
from companies.models import Store

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


class ProductUploadExcelView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        excel_file = request.FILES.get('file')
        store_id = request.data.get('store')

        if not excel_file or not store_id:
            return Response({"error": "Se requiere archivo y store ID."}, status=400)

        try:
            store = Store.objects.get(id=store_id, company=request.user.company)
        except Store.DoesNotExist:
            return Response({"error": "Tienda inválida o no pertenece a tu empresa."}, status=403)

        wb = openpyxl.load_workbook(excel_file)
        sheet = wb.active
        headers = [cell.value for cell in sheet[1]]

        created = 0
        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = dict(zip(headers, row))
            title = row_data.get('title')
            image_url = row_data.get('image_url')

            if not title or not image_url:
                continue  # Salta filas incompletas

            Product.objects.create(
                company=request.user.company,
                store=store,
                title=title,
                image_url=image_url,
                source_type='excel',
                original_file_name=excel_file.name
            )
            created += 1

        return Response({"message": f"{created} productos creados exitosamente."}, status=201)