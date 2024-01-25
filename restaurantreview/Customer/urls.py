from django.urls import path
from .views import CustomerListAPIView

urlpatterns = [
    path('api/customers/', CustomerListAPIView.as_view(), name='customer-list'),
    # Add more URL patterns as needed for other views/APIs
]
