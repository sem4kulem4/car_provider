from django.db.models import Sum
from rest_framework import serializers

from .models import Order, CarModel, CarBrand, Color


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CarModel
        fields = (
            'model',
            'brand'
        )


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для безопасных запросов."""
    car = CarSerializer()
    color = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = (
            'pub_date',
            'color',
            'car',
            'amount'
        )


class CreateUpdateOrderSerializer(serializers.Serializer):
    """Сериализатор для создания и обновления заказов."""
    pub_date = serializers.DateTimeField(
        required=False,
        input_formats=('%Y-%m-%d',)
    )
    brand = serializers.CharField(max_length=200)
    model = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=100)
    amount = serializers.IntegerField(min_value=1)

    def validate(self, data):
        amount = int(data.get('amount'))
        if amount <= 0:
            raise serializers.ValidationError(
                'Количество должно быть больше 0!'
            )
        return data


class ColorSerializer(serializers.ModelSerializer):
    """Сериализатор для атрибутов цвет, количество."""
    count = serializers.SerializerMethodField(method_name='get_count')

    class Meta:
        model = Color
        fields = (
            'color',
            'count'
        )

    def get_count(self, obj):
        count = Order.objects.filter(color=obj).aggregate(Sum('amount'))
        return count.get('amount__sum') or 0

class BrandSerializer(serializers.ModelSerializer):
    """Сериализатор для атрибутов марка, количество."""
    count = serializers.SerializerMethodField(method_name='get_count')

    class Meta:
        model = CarBrand
        fields = (
            'brand',
            'count'
        )

    def get_count(self, obj):
        count = Order.objects.filter(car__brand__brand=obj).aggregate(Sum('amount'))
        return count.get('amount__sum') or 0