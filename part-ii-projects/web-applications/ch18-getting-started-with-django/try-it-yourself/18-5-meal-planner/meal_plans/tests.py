"""Tests for the meal_plans app, for exercise 18-5."""

from django.test import TestCase


class HomePageTests(TestCase):
    """Check the Meal Planner home page."""

    def test_home_page_loads(self) -> None:
        """The home page should load, using its own template."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "meal_plans/index.html")

    def test_home_page_shows_the_title(self) -> None:
        """The home page should show the words Meal Planner."""
        response = self.client.get("/")
        self.assertContains(response, "Meal Planner")
