from django.urls import path
from .views import CustomerListAPIView, CustomerDetailAPIView, CustomerOrderAPIView, CustomerIssueAPIView

urlpatterns = [
    path('api/customers/', CustomerListAPIView.as_view(), name='customer-list'),
    path('api/customers/<int:pk>/', CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('api/customers/<int:id>/orders/', CustomerOrderAPIView.as_view(), name='customer-orders'),
    path('api/customers/<int:id>/issues/', CustomerIssueAPIView.as_view(), name='customer-issues'),


]
