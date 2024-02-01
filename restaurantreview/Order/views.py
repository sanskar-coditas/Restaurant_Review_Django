# order/views.py
from rest_framework import generics
from .models import Order
from .serializers import OrderCreateSerializer
from .serializers import OrderGetSerializer
from Menu.models import Menu
from Menu.serializers import MenuSerializer

class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return OrderGetSerializer

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderGetSerializer

class OrderMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        order_id = self.kwargs['id']
        return Order.objects.get(id=order_id).menu_items.all()
