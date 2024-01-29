# issue/models.py
from django.db import models
from Order.models import Order  # Import the Order model
from Customer.models import Customer  # Import the Customer model

class Issue(models.Model):
    description = models.TextField()
    order = models.ForeignKey(Order, related_name='issues', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Issue #{self.id} - Order: {self.order.id}, Customer: {self.customer.name}"
