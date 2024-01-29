from rest_framework import generics
from .models import Restaurant
from .serializers import RestaurantSerializer
from Menu.models import Menu  
from Menu.serializers import MenuSerializer  
from Order.models import Order
from Order.serializers import OrderSerializer


class RestaurantListAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['id']
        return Menu.objects.filter(restaurant_id=restaurant_id)
    
class RestaurantOrderAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        restaurant_id = self.kwargs['id']
        return Order.objects.filter(restaurant__id=restaurant_id)