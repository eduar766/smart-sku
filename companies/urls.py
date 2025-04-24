from django.urls import path
from .views import CompanyCreateView, StoreListCreateView

urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name='create-company'),
    path('stores/', StoreListCreateView.as_view(), name='stores-list-create'),
]