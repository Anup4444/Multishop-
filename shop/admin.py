from django.contrib import admin
from .models import Customer, Category, Product, Cart, cartProduct, Order, Admin

# Register your models here.
admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(cartProduct)
admin.site.register(Order)
