# issues/serializers.py
from rest_framework import serializers
from .models import Issue
from Order.serializers import OrderGetSerializer

class IssueSerializer(serializers.ModelSerializer):
    order_details = OrderGetSerializer(source='order', read_only=True)

    class Meta:
        model = Issue
        fields = ['id', 'description', 'order', 'customer', 'order_details']
