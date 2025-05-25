from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'boletas', BoletaViewSet)
router.register(r'dispatch-orders', DispatchOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
