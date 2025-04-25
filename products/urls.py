from django.urls import path
from .views import ProductListCreateView, ProductUploadExcelView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='products'),
    path('upload-excel/', ProductUploadExcelView.as_view(), name='upload-excel'),
]