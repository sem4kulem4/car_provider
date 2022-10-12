from datetime import datetime

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters, mixins
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import CarModel, CarBrand, Color, Order
from .filters import BrandFilter
from .serializers import (
    CreateUpdateOrderSerializer,
    OrderSerializer,
    ColorSerializer,
    BrandSerializer
)


class ColorViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()


class BrandViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = BrandSerializer
    queryset = CarBrand.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = CreateUpdateOrderSerializer
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('amount',)
    filterset_class = BrandFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 10
    http_method_names = ('get', 'post', 'delete', 'put')

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list',):
            return OrderSerializer
        return CreateUpdateOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUpdateOrderSerializer(
            data=self.request.data,
            many=False
        )
        serializer.is_valid(raise_exception=True)
        pub_date = serializer.validated_data.get('pub_date', datetime.now().strftime('%Y-%m-%d'))
        brand = serializer.validated_data.get('brand').lower()
        model = serializer.validated_data.get('model').lower()
        color = serializer.validated_data.get('color').lower()
        amount = serializer.validated_data.get('amount')

        color, created = Color.objects.get_or_create(color=color)
        car_brand, created = CarBrand.objects.get_or_create(brand=brand)
        car, created = CarModel.objects.get_or_create(brand_id=car_brand.id, model=model)
        Order.objects.create(
            color_id=color.id,
            car_id=car.id,
            amount=amount,
            pub_date=pub_date
        )
        return Response(
            data=serializer.validated_data,
            status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        serializer = CreateUpdateOrderSerializer(
            data=self.request.data,
            many=False
        )
        serializer.is_valid(raise_exception=True)
        pub_date = serializer.validated_data.get('pub_date', datetime.now().strftime('%Y-%m-%d'))
        brand = serializer.validated_data.get('brand').lower()
        model = serializer.validated_data.get('model').lower()
        color = serializer.validated_data.get('color').lower()
        amount = serializer.validated_data.get('amount')

        order = get_object_or_404(Order, id=self.kwargs.get('pk'))
        color, created = Color.objects.get_or_create(color=color)
        car_brand, created = CarBrand.objects.get_or_create(brand=brand)
        car, created = CarModel.objects.get_or_create(brand_id=car_brand.id, model=model)

        order.color_id = color.id
        order.car_id = car.id
        order.amount = amount
        order.pub_date = pub_date
        order.save()
        return Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )
