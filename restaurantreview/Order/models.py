# order/models.py
from django.db import models
from Customer.models import Customer 
from Restaurant.models import Restaurant 
from Menu.models import Menu


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    menu_items = models.ManyToManyField(Menu)


    def __str__(self):
        return f"Order #{self.id} - Customer: {self.customer.name} - Restaurant: {self.restaurant.name}"
