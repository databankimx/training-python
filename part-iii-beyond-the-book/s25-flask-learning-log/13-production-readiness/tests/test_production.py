"""Tests for production readiness, for chapter 13 of the Flask Learning Log."""

import os
import unittest
from unittest import mock

from flask_log import create_app

IN_MEMORY = {"DATABASE_URL": "sqlite:///:memory:", "TESTING": True}


class ProductionReadinessTests(unittest.TestCase):
    """Check the error pages, the settings that come from the environment, and the settings check."""

    def test_unknown_address_gets_the_friendly_404_page(self) -> None:
        """An address that doesn't exist should show the Learning Log page, with a way back home."""
        app = create_app(IN_MEMORY)
        response = app.test_client().get("/no-such-page/")
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"Page not found", response.data)

    def test_server_error_gets_the_friendly_500_page_when_debug_is_off(self) -> None:
        """With debug off, an unexpected error should show the friendly page, not the traceback."""
        app = create_app({"DATABASE_URL": "sqlite:///:memory:", "TESTING": False, "DEBUG": False})

        def broken():
            raise RuntimeError("something unexpected")

        app.add_url_rule("/broken/", "broken", broken)
        response = app.test_client().get("/broken/")
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Something went wrong", response.data)

    def test_secret_key_comes_from_the_environment(self) -> None:
        """The session secret key should be read from LL_SECRET_KEY, so it's not kept in the code."""
        with mock.patch.dict(os.environ, {"LL_SECRET_KEY": "a-test-secret-value"}):
            app = create_app(IN_MEMORY)
        self.assertEqual(app.config["SECRET_KEY"], "a-test-secret-value")

    def test_database_url_comes_from_the_environment(self) -> None:
        """The database address should be read from DATABASE_URL, which is where a connection string goes."""
        with mock.patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}):
            app = create_app({"TESTING": True})
        self.assertEqual(app.config["DATABASE_URL"], "sqlite:///:memory:")

    def test_session_cookie_is_secure_only_when_debug_is_off(self) -> None:
        """With debug off, the session cookie should be marked secure, so it's sent only over HTTPS."""
        with mock.patch.dict(os.environ, {"LL_DEBUG": "0"}):
            live_app = create_app(IN_MEMORY)
        with mock.patch.dict(os.environ, {"LL_DEBUG": "1"}):
            local_app = create_app(IN_MEMORY)
        self.assertTrue(live_app.config["SESSION_COOKIE_SECURE"])
        self.assertFalse(local_app.config["SESSION_COOKIE_SECURE"])

    def test_check_settings_reports_debug_and_the_default_key(self) -> None:
        """With debug on and no secret key set, check-settings should say so, and change nothing."""
        with mock.patch.dict(os.environ, {"LL_DEBUG": "1"}):
            os.environ.pop("LL_SECRET_KEY", None)
            app = create_app(IN_MEMORY)
            result = app.test_cli_runner().invoke(args=["check-settings"])
        self.assertIn("Debug mode is on", result.output)
        self.assertIn("default secret key", result.output)

    def test_check_settings_is_quiet_when_the_site_is_ready(self) -> None:
        """With debug off and a real secret key, check-settings should say the settings look ready."""
        with mock.patch.dict(os.environ, {"LL_DEBUG": "0", "LL_SECRET_KEY": "a-very-long-random-secret-value"}):
            app = create_app(IN_MEMORY)
            result = app.test_cli_runner().invoke(args=["check-settings"])
        self.assertIn("Settings look ready for a live site.", result.output)
