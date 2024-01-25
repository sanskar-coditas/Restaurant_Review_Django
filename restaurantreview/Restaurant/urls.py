from django.urls import path
from .views import RestaurantListAPIView

urlpatterns = [
    path('api/restaurants/', RestaurantListAPIView.as_view(), name='restaurant-list'),
    # Add more URL patterns as needed for other views/APIs
]