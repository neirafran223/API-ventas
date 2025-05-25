from rest_framework import viewsets
from .models import Product, Cart, CartItem, Boleta, DispatchOrder
from .serializers import *

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class BoletaViewSet(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer

class DispatchOrderViewSet(viewsets.ModelViewSet):
    queryset = DispatchOrder.objects.all()
    serializer_class = DispatchOrderSerializer
