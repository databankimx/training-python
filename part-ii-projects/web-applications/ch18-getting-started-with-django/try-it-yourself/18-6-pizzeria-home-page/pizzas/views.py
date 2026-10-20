"""The views for the pizzas app. A view receives a request and returns a response."""

from django.shortcuts import render


def index(request):
    """The home page for the Pizzeria."""
    return render(request, "pizzas/index.html")
