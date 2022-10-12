from django.contrib import admin

from .models import CarBrand, CarModel, Color, Order

admin.site.register(CarBrand)
admin.site.register(CarModel)
admin.site.register(Color)
admin.site.register(Order)
