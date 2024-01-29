# order/views.py
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from Menu.models import Menu  # Import the Menu model
from Menu.serializers import MenuSerializer  

class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderMenuAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

