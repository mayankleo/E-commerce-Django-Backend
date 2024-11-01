from django.contrib import admin
from .models import Product, Category, ProductImage  

# Define an inline admin descriptor for ProductImage model
class ProductImageInline(admin.TabularInline):  # Or admin.StackedInline for a vertical layout
    model = ProductImage
    extra = 1  # Number of extra forms to show by default

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_registered", "product_price", "product_quantity", "product_in_stock"]
    inlines = [ProductImageInline]  
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
