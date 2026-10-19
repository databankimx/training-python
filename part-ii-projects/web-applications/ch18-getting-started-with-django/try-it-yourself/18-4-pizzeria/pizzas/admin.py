"""Register the pizzas models with the Django admin site."""

from django.contrib import admin

from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
