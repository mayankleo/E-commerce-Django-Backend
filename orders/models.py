from django.db import models
from products.models import Product
from users.models import Customer


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        max_length=10,
        choices=[
            ("Pending", "Pending"),
            ("Shipped", "Shipped"),
            ("Delivered", "Delivered"),
            ("Cancelled", "Cancelled"),
            ("Refunded", "Refunded"),
        ],
        default="Pending",
    )
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, editable=False
    )
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order_quantity = models.PositiveIntegerField(default=1)
    order_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.order_price = self.order_product.product_price
        self.order_total = self.order_price * self.order_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_customer.customer.username} | {self.order_product.product_name}"
