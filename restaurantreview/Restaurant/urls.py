from django.urls import path
from .views import RestaurantListAPIView, RestaurantDetailAPIView, RestaurantMenuAPIView, RestaurantOrderAPIView

urlpatterns = [
    path('api/restaurants/', RestaurantListAPIView.as_view(), name='restaurant-list'),
    path('api/restaurants/<int:pk>/', RestaurantDetailAPIView.as_view(), name='restaurant-detail'),
    path('api/restaurants/<int:id>/menu/', RestaurantMenuAPIView.as_view(), name='restaurant-menu'),
    path('api/restaurants/<int:id>/orders/', RestaurantOrderAPIView.as_view(), name='restaurant-order'),


]