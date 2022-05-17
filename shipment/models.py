from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_supplier = models.BooleanField('supplier', default=False)
    is_customer = models.BooleanField('customer', default=False)


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    info = models.CharField(max_length=200, null= True, default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Shipment(models.Model):
    STATUS = (
        ("Sending", "sending"),
    ("Pending", "Pending"),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('In way', 'In way'),
    ('Arrived Destination', 'Arrived Destination'),
    ("Received", "Received")
    )
    orderid = models.CharField(max_length=20, unique=True)
    product_name = models.ForeignKey(Product, on_delete=models.PROTECT, default="1")
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    shipping_address = models.CharField(max_length=50)
    order_amount = models.IntegerField(default=0)
    supplier = models.ForeignKey(User, on_delete=models.PROTECT, related_name='supplier')
    customer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customer')

    def __str__(self):
        return f'{self.product_name}'