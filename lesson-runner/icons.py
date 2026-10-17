"""Vector icons and the DataBank logo, drawn in code so they don't depend on any font."""

from __future__ import annotations
import math

from PySide6.QtCore import QPointF, QRectF, Qt #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QColor, QIcon, QPainter, QPainterPath, QPen, QPixmap, QPolygonF #pylint: disable=no-name-in-module #NOSONAR

import logo

#pylint: disable=too-many-branches, too-many-statements

def draw_icon(kind: str, color: str, size: int = 18) -> QIcon:
    """Vector icons, drawn in code so they don't depend on any font."""
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    pen = QPen(QColor(color), 1.6)
    pen.setCapStyle(Qt.PenCapStyle.RoundCap)
    pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
    painter.setPen(pen)
    painter.setBrush(Qt.BrushStyle.NoBrush)
    s = size / 18.0
    if kind == "copy":
        painter.drawRoundedRect(QRectF(3.5 * s, 5.5 * s, 9 * s, 9.5 * s), 2 * s, 2 * s)
        painter.drawRoundedRect(QRectF(6.5 * s, 2.5 * s, 9 * s, 9.5 * s), 2 * s, 2 * s)
    elif kind == "popout":
        painter.drawLine(QPointF(5 * s, 13 * s), QPointF(13 * s, 5 * s))
        painter.drawLine(QPointF(7 * s, 5 * s), QPointF(13 * s, 5 * s))
        painter.drawLine(QPointF(13 * s, 5 * s), QPointF(13 * s, 11 * s))
    elif kind == "dock":
        painter.drawLine(QPointF(13 * s, 5 * s), QPointF(5 * s, 13 * s))
        painter.drawLine(QPointF(5 * s, 7 * s), QPointF(5 * s, 13 * s))
        painter.drawLine(QPointF(5 * s, 13 * s), QPointF(11 * s, 13 * s))
    elif kind == "check":
        painter.drawPolyline(QPolygonF([QPointF(3.5 * s, 9.5 * s), QPointF(7.5 * s, 13.5 * s),
                                        QPointF(14.5 * s, 5.5 * s)]))
    elif kind == "sun":
        painter.drawEllipse(QPointF(9 * s, 9 * s), 3.5 * s, 3.5 * s)
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            inner = QPointF(9 * s + 6 * s * math.cos(rad), 9 * s + 6 * s * math.sin(rad))
            outer = QPointF(9 * s + 8 * s * math.cos(rad), 9 * s + 8 * s * math.sin(rad))
            painter.drawLine(inner, outer)
    elif kind == "moon":
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(color))
        outer = QPainterPath()
        outer.addEllipse(QPointF(9 * s, 9 * s), 6.5 * s, 6.5 * s)
        cut = QPainterPath()
        cut.addEllipse(QPointF(12.5 * s, 6.5 * s), 5.5 * s, 5.5 * s)
        painter.drawPath(outer.subtracted(cut))
    elif kind == "window":
        painter.drawRoundedRect(QRectF(2.5 * s, 3.5 * s, 13 * s, 11 * s), 1.5 * s, 1.5 * s)
        painter.drawLine(QPointF(2.5 * s, 6.5 * s), QPointF(15.5 * s, 6.5 * s))
    elif kind == "globe":
        painter.drawEllipse(QPointF(9 * s, 9 * s), 6.5 * s, 6.5 * s)
        painter.drawEllipse(QRectF(5.5 * s, 2.5 * s, 7 * s, 13 * s))
        painter.drawLine(QPointF(2.5 * s, 9 * s), QPointF(15.5 * s, 9 * s))
    elif kind == "keyboard":
        painter.drawRoundedRect(QRectF(1.5 * s, 4.5 * s, 15 * s, 9 * s), 1.5 * s, 1.5 * s)
        for x in (4, 7, 10, 13):
            painter.drawPoint(QPointF(x * s, 7.5 * s))
        painter.drawLine(QPointF(5 * s, 11 * s), QPointF(13 * s, 11 * s))
    elif kind == "disk":
        painter.drawRoundedRect(QRectF(3 * s, 3 * s, 12 * s, 12 * s), 1.5 * s, 1.5 * s)
        painter.drawRect(QRectF(6 * s, 3 * s, 6 * s, 4 * s))
        painter.drawRect(QRectF(5 * s, 10 * s, 8 * s, 5 * s))
    elif kind == "cloud":
        painter.drawEllipse(QRectF(2 * s, 8 * s, 7 * s, 5 * s))
        painter.drawEllipse(QRectF(5 * s, 5 * s, 8 * s, 7 * s))
        painter.drawEllipse(QRectF(9 * s, 8 * s, 6 * s, 5 * s))
    painter.end()
    return QIcon(pixmap)


def logo_pixmap(size: int, color: str) -> QPixmap:
    """The DataBank logo as a transparent, antialiased pixmap."""
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor(color))
    scale = size / logo.SIZE
    for polygon in logo.shapes():
        painter.drawPolygon(QPolygonF([QPointF(x * scale, y * scale) for x, y in polygon]))
    painter.end()
    return pixmap
