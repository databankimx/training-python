"""The models for the pizzas app. A model describes the data the app stores."""

from django.db import models


class Pizza(models.Model):
    """A named pizza on the menu, such as Hawaiian or Meat Lovers."""

    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        """Return the pizza's name."""
        return self.name


class Topping(models.Model):
    """One topping on a pizza, such as pineapple or sausage."""

    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        """Return the topping's name."""
        return self.name
