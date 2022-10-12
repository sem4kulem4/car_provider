from django.urls import path, include
from rest_framework import routers

from .views import BrandViewSet, ColorViewSet, OrderViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('color', ColorViewSet, basename='color')
router.register('brand', BrandViewSet, basename='brand')
urlpatterns = [
   path('', include(router.urls)),
]
