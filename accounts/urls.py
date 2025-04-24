from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, CustomLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='custom-login'),
]