from django.contrib import admin
from .models import Product, Cart, CartItem, Boleta, DispatchOrder

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Boleta)
admin.site.register(DispatchOrder)
