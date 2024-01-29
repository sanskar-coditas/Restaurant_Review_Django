# order/serializers.py
from rest_framework import serializers
from .models import Order
from Menu.serializers import MenuSerializer


class OrderSerializer(serializers.ModelSerializer):
    menu_items = MenuSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'total_amount', 'created_at', 'menu_items']
