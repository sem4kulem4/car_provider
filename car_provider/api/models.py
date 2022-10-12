from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Color(models.Model):
    color = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Цвет'
    )

    def __str__(self):
        return f'{self.color}'


class CarBrand(models.Model):
    brand = models.CharField(
        unique=True,
        max_length=200,
        verbose_name='Марка машины'
    )

    def __str__(self):
        return f'{self.brand}'


class CarModel(models.Model):
    brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
        verbose_name='Марка машины'
    )
    model = models.CharField(
        max_length=200,
        verbose_name='Модель машины'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('brand', 'model'),
                name='unique_car_name'
            )
        ]

    def __str__(self):
        return f'{self.model}'


class Order(models.Model):
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        verbose_name='Цвет машины в заказе'
    )
    car = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
        verbose_name='Модель машины в заказе'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество заданных машин'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата заказа'
    )

    def __str__(self):
        return f'{self.color} {self.car} - {self.amount}'
