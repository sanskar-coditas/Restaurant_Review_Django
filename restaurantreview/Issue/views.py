# issue/views.py
from rest_framework import generics
from .models import Issue
from .serializers import IssueSerializer
from Order.models import Order
from Order.serializers import OrderSerializer

class IssueListAPIView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueOrderDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        issue_id = self.kwargs['id']
        issue = Issue.objects.get(id=issue_id)
        order_id = issue.order_id
        order = Order.objects.get(id=order_id)
        return order

