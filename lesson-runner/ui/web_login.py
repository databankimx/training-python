"""The dialog that asks for the admin account's username and password, once per runner session."""

from __future__ import annotations

import re

from PySide6.QtWidgets import (QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit,  #pylint: disable=no-name-in-module #NOSONAR
                               QMessageBox, QVBoxLayout)

from config import DARK

USERNAME = re.compile(r"^[a-z0-9]+$")
MIN_PASSWORD = 8


class AdminLoginDialog(QDialog):
    """Asks for a username and a password, and checks them before accepting."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Admin account")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(
            "Choose a username and password for the admin account.\n"
            "They're used for this session only, and are never saved to disk.\n\n"
            "Username: lowercase letters and numbers only.\n"
            "Password: at least 8 characters."))

        form = QFormLayout()
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm = QLineEdit()
        self.confirm.setEchoMode(QLineEdit.EchoMode.Password)
        form.addRow("Username", self.username)
        form.addRow("Password", self.password)
        form.addRow("Repeat password", self.confirm)
        layout.addLayout(form)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._check_and_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        # Style the buttons with the runner's accent colour, so they look clickable and react to the mouse.
        self.setStyleSheet(
            "QPushButton {"
            f" background: {DARK['accent']}; color: #FFFFFF; border: none;"
            " padding: 6px 18px; border-radius: 3px; }"
            f"QPushButton:hover {{ background: {DARK['accent_hover']}; }}"
            f"QPushButton:pressed {{ background: {DARK['selection']}; }}"
        )

    def _check_and_accept(self) -> None:
        """Accept the details only when they follow the rules."""
        if not USERNAME.match(self.username.text().strip()):
            QMessageBox.warning(self, "Check the username", "Use lowercase letters and numbers only.")
            return
        if len(self.password.text()) < MIN_PASSWORD:
            QMessageBox.warning(self, "Check the password", "Use at least 8 characters.")
            return
        if self.password.text() != self.confirm.text():
            QMessageBox.warning(self, "Check the password", "The two passwords don't match.")
            return
        self.accept()

    def credentials(self) -> tuple[str, str]:
        """The username and password the student entered."""
        return self.username.text().strip(), self.password.text()
