"""Tests for the Bootstrap setup in chapter 20, step 1."""

from django.conf import settings
from django.template import Context, Engine
from django.test import SimpleTestCase


class BootstrapSetupTests(SimpleTestCase):
    """Check that django-bootstrap5 is installed and its template tags load."""

    def test_bootstrap_app_is_installed(self) -> None:
        """The django_bootstrap5 app should be listed in INSTALLED_APPS."""
        self.assertIn("django_bootstrap5", settings.INSTALLED_APPS)

    def test_bootstrap_template_tags_load(self) -> None:
        """A template that loads the Bootstrap tags should compile and render without error."""
        template = Engine.get_default().from_string("{% load django_bootstrap5 %}{% bootstrap_css %}")
        rendered = template.render(Context({}))
        self.assertIn("bootstrap", rendered.lower())
