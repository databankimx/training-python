"""Tests for accounts, for chapter 9 of the Flask Learning Log."""

import html
import os
import unittest
from unittest import mock

from flask_log import create_app
from flask_log.database import Base
from flask_log.models import User


class AccountTests(unittest.TestCase):
    """Check registering, logging in, logging out, and the admin account."""

    def setUp(self) -> None:
        """Build the app with its own database, and make a user called sam who can sign in."""
        self.app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": True})
        Base.metadata.create_all(self.app.extensions["engine"])
        with self.app.extensions["session_factory"]() as session:
            sam = User(username="sam")
            sam.set_password("a-long-password-1")
            session.add(sam)
            session.commit()
        self.client = self.app.test_client()

    def signed_in_user_id(self):
        """The user id stored in the session, or None when nobody is signed in."""
        with self.client.session_transaction() as session:
            return session.get("user_id")

    def test_register_page_loads(self) -> None:
        """The register form should load, with a password box in it."""
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'type="password"', response.data)

    def test_register_creates_an_account_and_signs_in(self) -> None:
        """A valid registration should create the user, sign them in, and send them to the home page."""
        response = self.client.post("/accounts/register/", data={
            "username": "alex", "password": "another-password-2", "confirm": "another-password-2"})
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(self.signed_in_user_id())

    def test_register_rejects_mismatched_passwords(self) -> None:
        """Passwords that don't match should be refused, with a message, and nothing is saved."""
        response = self.client.post("/accounts/register/", data={
            "username": "alex", "password": "another-password-2", "confirm": "different-password-3"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("The two passwords don't match.", html.unescape(response.get_data(as_text=True)))
        self.assertIsNone(self.signed_in_user_id())

    def test_login_with_the_right_password_signs_in(self) -> None:
        """The right password should sign sam in."""
        response = self.client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})
        self.assertEqual(response.status_code, 302)
        self.assertIsNotNone(self.signed_in_user_id())

    def test_login_with_the_wrong_password_is_refused(self) -> None:
        """A wrong password should not sign anyone in, and the form should say so."""
        response = self.client.post("/accounts/login/", data={"username": "sam", "password": "guess-the-password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("That username and password don't match.", html.unescape(response.get_data(as_text=True)))
        self.assertIsNone(self.signed_in_user_id())

    def test_logout_clears_the_session(self) -> None:
        """Logging out should remove the signed-in user from the session."""
        self.client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})
        self.client.post("/accounts/logout/")
        self.assertIsNone(self.signed_in_user_id())

    def test_navigation_bar_shows_the_signed_in_name(self) -> None:
        """Once signed in, every page should greet the user by name in the navigation bar."""
        self.client.post("/accounts/login/", data={"username": "sam", "password": "a-long-password-1"})
        response = self.client.get("/")
        self.assertIn(b"Hello, sam.", response.data)

    def test_create_admin_makes_the_account_from_the_environment(self) -> None:
        """The create-admin command should make the admin account from the two environment variables."""
        with mock.patch.dict(os.environ, {"STUDENT_ADMIN_USERNAME": "admin1", "STUDENT_ADMIN_PASSWORD": "admin-password-1"}):
            result = self.app.test_cli_runner().invoke(args=["create-admin"])
        self.assertEqual(result.exit_code, 0)
        with self.app.extensions["session_factory"]() as session:
            admin = session.query(User).filter_by(username="admin1").one()
            self.assertTrue(admin.check_password("admin-password-1"))
