"""The views for the pizzas app. A view receives a request and returns a response."""

from django.shortcuts import get_object_or_404, render

from .models import Pizza, Topping


def index(request):
    """The home page for the Pizzeria."""
    return render(request, "pizzas/index.html")


def pizzas(request):
    """Show the names of every pizza on the menu."""
    pizzas = Pizza.objects.all()
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)


def pizza(request, pizza_id):
    """Show one pizza and its toppings."""
    pizza = get_object_or_404(Pizza, id=pizza_id)
    toppings = Topping.objects.filter(pizza=pizza)
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)
