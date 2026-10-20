"""Tests for the pizzas app, for exercises 18-4, 18-6 and 18-8."""

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


class PizzeriaHomePageTests(TestCase):
    """Check the Pizzeria home page."""

    def test_home_page_loads(self) -> None:
        """The home page should load, using its own template."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pizzas/index.html")

    def test_home_page_links_back_to_itself(self) -> None:
        """The shared top bar should link to the home page."""
        response = self.client.get("/")
        self.assertContains(response, 'href="/"')


class PizzaPagesTests(TestCase):
    """Check the list of pizzas and the page for each pizza."""

    def setUp(self) -> None:
        """Make a pizza with two toppings."""
        self.pizza = Pizza.objects.create(name="Hawaiian")
        Topping.objects.create(pizza=self.pizza, name="pineapple")
        Topping.objects.create(pizza=self.pizza, name="Canadian bacon")

    def test_pizzas_page_loads(self) -> None:
        """The list of pizzas should load, using its own template."""
        response = self.client.get("/pizzas/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pizzas/pizzas.html")

    def test_pizzas_page_links_to_each_pizza(self) -> None:
        """Each pizza's name should link to its own page."""
        response = self.client.get("/pizzas/")
        self.assertContains(response, "Hawaiian")
        self.assertContains(response, f'href="/pizzas/{self.pizza.id}/"')

    def test_pizza_page_shows_its_toppings(self) -> None:
        """A pizza's page should show its name and each of its toppings."""
        response = self.client.get(f"/pizzas/{self.pizza.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hawaiian")
        self.assertContains(response, "pineapple")
        self.assertContains(response, "Canadian bacon")

    def test_missing_pizza_returns_not_found(self) -> None:
        """A pizza that doesn't exist should give a 404 page, not an error."""
        response = self.client.get("/pizzas/9999/")
        self.assertEqual(response.status_code, 404)
