"""Fonts and the application stylesheet."""

from __future__ import annotations

from PySide6.QtGui import QFont, QFontDatabase #pylint: disable=no-name-in-module #NOSONAR

from config import CODE_FAMILIES

#pylint: disable=line-too-long

def code_font(size: int) -> QFont:
    """The first installed monospace font from CODE_FAMILIES, with a fixed-pitch fallback."""
    installed = set(QFontDatabase.families())
    family = next((name for name in CODE_FAMILIES if name in installed), "Consolas")
    font = QFont(family, size)
    font.setStyleHint(QFont.StyleHint.Monospace)
    font.setFixedPitch(True)
    return font


def stylesheet(c: dict[str, str]) -> str:
    """Application stylesheet for one palette. Fonts are set in code, not here."""
    return f"""
    QMainWindow, QWidget#root {{ background: {c['bg']}; }}
    QWidget {{ color: {c['fg']}; }}
    QLabel#title {{ font-size: 14pt; font-weight: bold; }}
    QLabel#subtitle, QLabel#section {{ color: {c['muted']}; }}
    QLabel#section {{ font-size: 8pt; font-weight: bold; padding: 4px 10px; }}
    QFrame#badge {{ background: {c['badge']}; border-radius: 9px; }}
    QLabel#badgeText {{ color: {c['fg']}; font-size: 8pt; font-weight: bold; }}
    QFrame#header {{ background: {c['accent']}; }}
    QLabel#headerText {{ color: white; font-size: 13pt; font-weight: bold; }}
    QTreeWidget, QListWidget {{ background: {c['panel']}; border: none; outline: 0; }}
    QTreeWidget::item {{ padding: 0px 2px; }}
    QTreeWidget::item:selected, QListWidget::item:selected {{
        background: {c['accent']}; color: white; }}
    QListWidget::item {{ padding: 0px 10px; }}
    QPlainTextEdit {{ background: {c['bg']}; border: none; }}
    QLineEdit {{ background: {c['bg']}; border: 1px solid {c['border']}; padding: 3px 6px; }}
    QPushButton {{ background: transparent; border: none; color: {c['muted']}; padding: 4px 8px; }}
    QPushButton#run {{ background: {c['accent']}; color: white; font-weight: bold;
                       padding: 6px 16px; border-radius: 3px; }}
    QPushButton#run:disabled {{ background: {c['border']}; color: {c['fg']}; }}
    QPushButton#continue {{ background: {c['accent']}; color: white; font-weight: bold;
                            padding: 4px 12px; }}
    QToolButton {{ background: transparent; border: none; padding: 4px; border-radius: 3px; }}
    QToolButton:hover {{ background: {c['border']}; }}
    QTabWidget::pane {{ border: none; }}
    QTabBar::tab {{ background: {c['panel']}; color: {c['muted']}; padding: 6px 14px; }}
    QTabBar::tab:selected {{ background: {c['bg']}; color: {c['fg']}; font-weight: bold; }}
    QFrame#resetBar {{ background: {c['panel']}; }}
    QSplitter::handle {{ background: {c['border']}; }}
    """


def tooltip_style(c: dict[str, str]) -> str:
    """Application-level style for tooltips. Tooltips are separate popups, so the window's sheet doesn't reach them."""
    return (f"QToolTip {{ background: {c['panel']}; color: {c['fg']}; border: 1px solid {c['border']};"
            f" padding: 4px 6px; }}")
