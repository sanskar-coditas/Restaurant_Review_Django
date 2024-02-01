# order/serializers.py
from rest_framework import serializers
from .models import Order
from Menu.serializers import MenuSerializer
from Menu.models import Menu

class OrderGetSerializer(serializers.ModelSerializer):
    menu_items = MenuSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'total_amount', 'created_at', 'menu_items']


class OrderCreateSerializer(serializers.ModelSerializer):
    menu_items = serializers.PrimaryKeyRelatedField(many=True, queryset=Menu.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'total_amount', 'created_at', 'menu_items']