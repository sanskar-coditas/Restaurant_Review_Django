# order/urls.py
from django.urls import path
from .views import OrderListAPIView, OrderDetailAPIView, OrderMenuAPIView

urlpatterns = [
    path('api/orders/', OrderListAPIView.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('api/orders/<int:id>/menu/', OrderMenuAPIView.as_view(), name='order-menu'),

]
