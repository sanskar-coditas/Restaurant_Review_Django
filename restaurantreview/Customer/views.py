from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from Order.serializers import OrderSerializer
from Order.models import Order
from Issue.serializers import IssueSerializer
from Issue.models import Issue

class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerOrderAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer_id = self.kwargs['id']
        return Order.objects.filter(customer_id=customer_id)
    

class CustomerIssueAPIView(generics.ListAPIView):
    serializer_class = IssueSerializer

    def get_queryset(self):
        customer_id = self.kwargs['id']
        return Issue.objects.filter(customer_id=customer_id)
