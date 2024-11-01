from django.contrib import admin
from .models import Customer 

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer", "customer_verified"]
    # list_filter = ('is_staff', 'is_active')
    # search_fields = ('username', 'email')

admin.site.register(Customer, CustomerAdmin)

