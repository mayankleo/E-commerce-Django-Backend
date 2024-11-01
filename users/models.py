from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=12)
    customer_address = models.TextField(max_length=100)
    customer_city = models.CharField(max_length=50)
    customer_state = models.CharField(max_length=50)
    customer_zip_code = models.CharField(max_length=6)
    customer_country = models.CharField(max_length=50)
    customer_registered = models.DateTimeField(auto_now_add=True, editable=False)
    customer_updated = models.DateTimeField(auto_now=True)
    customer_verified = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} | {self.customer.username}"

