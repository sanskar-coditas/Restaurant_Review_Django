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

class OrderMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        order_id = self.kwargs['id']
        return Order.objects.get(id=order_id).menu_items.all()

