from django.contrib.auth.models import AbstractUser
from django.db import models


class Widgets(models.Model):
    name = models.CharField(max_length=20)

<<<<<<< HEAD
    def __str__(self):
        return f"{self.name}"
=======

# class WidgetsForUser(models.Model):
#     user = models.ForeignKey()
#     widgets=models.ForeignKey()
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    info = models.CharField(max_length=200, null=True, default="")
    price = models.IntegerField(default=0)


class User(AbstractUser):
    is_supplier = models.BooleanField("supplier", default=False, blank=True)
    is_customer = models.BooleanField("customer", default=False)


class Shipment(models.Model):
    STATUS = (
        ("Sending", "sending"),
        ("Pending", "Pending"),
        ("Packed", "Packed"),
        ("Shipped", "Shipped"),
        ("In way", "In way"),
        ("Arrived Destination", "Arrived Destination"),
        ("Received", "Received"),
    )
    orderid = models.CharField(max_length=20, unique=True)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, default="1")
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    shipping_address = models.CharField(max_length=50)
    order_amount = models.IntegerField(default=0)
    supplier = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="supplier"
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer"
    )

    def __str__(self):
        return f"{self.product_name}"

<<<<<<< HEAD

class UserConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userwidget")
    widget = models.ManyToManyField(Widgets, related_name="userconfig")
=======

class UserConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    widget = models.ManyToManyField(Widgets)
    # status = models.BooleanField(default=False, blank=True)


# class FreindRequest(models.Model):
#     sender  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
#     receiver  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
#     is_active = models.BooleanField(blank=True, null=False, default=True)
>>>>>>> ebceb8a7964ab8ab5834263b0e3dc7ad0effe4e7
