import os
import uuid
from django.db import models
from django.utils.text import slugify


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    product_id = instance.product_id.id if instance.product_id else "unknown_product"
    return os.path.join(f"dbimg/{product_id}/", filename)


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_description = models.TextField(max_length=200, blank=True)

    def delete(self, *args, **kwargs):
        general_category = Category.objects.get(
            category_name="General", category_description="Default Category"
        )
        Product.objects.filter(product_category=self).update(
            product_category=general_category
        )
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=200, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    product_registered = models.DateTimeField(auto_now_add=True, editable=False)
    product_quantity = models.PositiveIntegerField(default=0)
    product_in_stock = models.BooleanField(default=False, editable=False)
    product_updated = models.DateTimeField(auto_now=True)
    product_slug = models.SlugField(max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.product_in_stock = self.product_quantity > 0

        if not self.product_category:
            general_category = Category.objects.get(
                category_name="General", category_description="Default Category"
            )
            self.product_category = general_category

        if not self.product_slug:
            self.product_slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.ImageField(upload_to=get_file_path, blank=True, null=True)

    def __str__(self):
        return f"Image Of {self.product_id.product_name}"
