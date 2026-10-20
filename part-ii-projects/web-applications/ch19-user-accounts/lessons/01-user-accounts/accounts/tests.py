"""Tests for the accounts app and the top bar's sign-in links, for chapter 19, step 1."""

from django.contrib.auth.models import User
from django.test import TestCase


class AccountsTests(TestCase):
    """Check signing in, signing out, and registering."""

    def setUp(self) -> None:
        """Make an account that can sign in."""
        self.password = "a-long-test-password-1"
        self.user = User.objects.create_user("sam", "sam@example.com", self.password)

    def test_login_page_loads(self) -> None:
        """The login page should load, using Django's login template in our accounts app."""
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")

    def test_register_creates_and_signs_in_a_user(self) -> None:
        """A valid registration should create the account and sign the new user in."""
        response = self.client.post("/accounts/register/", {
            "username": "alex",
            "password1": "another-long-test-password-2",
            "password2": "another-long-test-password-2",
        })
        self.assertRedirects(response, "/")
        self.assertTrue(User.objects.filter(username="alex").exists())
        self.assertIn("_auth_user_id", self.client.session)

    def test_logout_ends_the_session(self) -> None:
        """Logging out should end the session, so the top bar offers the login link again."""
        self.client.login(username="sam", password=self.password)
        self.client.post("/accounts/logout/")
        response = self.client.get("/")
        self.assertContains(response, 'href="/accounts/login/"')

    def test_signed_in_user_sees_their_name(self) -> None:
        """The top bar should greet the signed-in user by name."""
        self.client.login(username="sam", password=self.password)
        response = self.client.get("/")
        self.assertContains(response, "Hello, sam.")

    def test_signed_out_visitor_sees_login_link(self) -> None:
        """A visitor who isn't signed in should see the login and register links."""
        response = self.client.get("/")
        self.assertContains(response, 'href="/accounts/login/"')
        self.assertContains(response, 'href="/accounts/register/"')
