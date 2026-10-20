"""Tests for the pizzas app, for exercise 18-4."""

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Pizza, Topping


class PizzaModelTests(TestCase):
    """Check the Pizza and Topping models."""

    def test_pizza_string_is_its_name(self) -> None:
        """A pizza should display as its name."""
        pizza = Pizza.objects.create(name="Hawaiian")
        self.assertEqual(str(pizza), "Hawaiian")

    def test_topping_string_is_its_name(self) -> None:
        """A topping should display as its name."""
        pizza = Pizza.objects.create(name="Hawaiian")
        topping = Topping.objects.create(pizza=pizza, name="pineapple")
        self.assertEqual(str(topping), "pineapple")

    def test_topping_belongs_to_its_pizza(self) -> None:
        """A topping should be linked to the pizza it's on."""
        pizza = Pizza.objects.create(name="Meat Lovers")
        topping = Topping.objects.create(pizza=pizza, name="sausage")
        self.assertEqual(topping.pizza, pizza)

    def test_deleting_a_pizza_deletes_its_toppings(self) -> None:
        """Toppings belong to a pizza, so they're removed along with it."""
        pizza = Pizza.objects.create(name="Hawaiian")
        Topping.objects.create(pizza=pizza, name="pineapple")
        pizza.delete()
        self.assertEqual(Topping.objects.count(), 0)


class PizzaAdminTests(TestCase):
    """Check that the pizzas and toppings can be seen in the admin site."""

    def setUp(self) -> None:
        """Create a superuser and sign them in."""
        self.user = User.objects.create_superuser("admin", "admin@example.com", "a-test-password")
        self.client.force_login(self.user)

    def test_pizza_list_is_in_admin(self) -> None:
        """The admin page for pizzas should load and show the pizzas."""
        Pizza.objects.create(name="Hawaiian")
        response = self.client.get("/admin/pizzas/pizza/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hawaiian")

    def test_topping_list_is_in_admin(self) -> None:
        """The admin page for toppings should load and show the toppings."""
        pizza = Pizza.objects.create(name="Hawaiian")
        Topping.objects.create(pizza=pizza, name="pineapple")
        response = self.client.get("/admin/pizzas/topping/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pineapple")
