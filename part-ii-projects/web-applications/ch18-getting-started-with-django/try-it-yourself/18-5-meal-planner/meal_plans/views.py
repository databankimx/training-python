"""The views for the meal_plans app. A view receives a request and returns a response."""

from django.shortcuts import render


def index(request):
    """The home page for the meal planner."""
    return render(request, "meal_plans/index.html")
