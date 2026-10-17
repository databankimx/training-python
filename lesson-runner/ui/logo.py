"""DataBank IMX logo, drawn from the two SVG paths in the WPF MainWindow.xaml.

The paths are converted to polygons in a 1000 x 1000 coordinate space, which
can then be drawn on a Canvas (nav header) or rasterised into a PhotoImage
(window icon). Nothing is read from an image file.
"""

from __future__ import annotations

import math
import tkinter as tk

SIZE = 1000.0
ARC_STEPS = 24
CUBIC_STEPS = 12


def _angle(ux: float, uy: float, vx: float, vy: float) -> float:
    """Signed angle from vector u to vector v, in radians."""
    return math.atan2(ux * vy - uy * vx, ux * vx + uy * vy)


def _arc_points(x1: float, y1: float, rx: float, ry: float,
                x2: float, y2: float, large: int, sweep: int) -> list[tuple[float, float]]:
    """Points along an SVG elliptical arc (no x-axis rotation), start excluded."""
    x1p, y1p = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    lam = (x1p * x1p) / (rx * rx) + (y1p * y1p) / (ry * ry)
    if lam > 1:
        rx *= math.sqrt(lam)
        ry *= math.sqrt(lam)
    num = rx * rx * ry * ry - rx * rx * y1p * y1p - ry * ry * x1p * x1p
    den = rx * rx * y1p * y1p + ry * ry * x1p * x1p
    coef = math.sqrt(max(0.0, num / den)) if den else 0.0
    if large == sweep:
        coef = -coef
    cxp = coef * rx * y1p / ry
    cyp = coef * -ry * x1p / rx
    cx = cxp + (x1 + x2) / 2.0
    cy = cyp + (y1 + y2) / 2.0

    ux, uy = (x1p - cxp) / rx, (y1p - cyp) / ry
    vx, vy = (-x1p - cxp) / rx, (-y1p - cyp) / ry
    theta1 = _angle(1.0, 0.0, ux, uy)
    delta = _angle(ux, uy, vx, vy)
    if sweep == 0 and delta > 0:
        delta -= 2 * math.pi
    elif sweep == 1 and delta < 0:
        delta += 2 * math.pi

    points = []
    for step in range(1, ARC_STEPS + 1):
        theta = theta1 + delta * step / ARC_STEPS
        points.append((cx + rx * math.cos(theta), cy + ry * math.sin(theta)))
    return points


def _cubic_points(p0, p1, p2, p3) -> list[tuple[float, float]]:
    """Points along a cubic Bezier curve, start excluded."""
    points = []
    for step in range(1, CUBIC_STEPS + 1):
        t = step / CUBIC_STEPS
        mt = 1 - t
        x = mt ** 3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t ** 3 * p3[0]
        y = mt ** 3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t ** 3 * p3[1]
        points.append((x, y))
    return points


def _first_shape() -> list[tuple[float, float]]:
    """M828.67,123.38 A497.9,497.9 0 0,0 500,0 H0 V639.49 Z"""
    start = (828.67, 123.38)
    points = [start]
    points += _arc_points(828.67, 123.38, 497.9, 497.9, 500.0, 0.0, 0, 0)
    points += [(0.0, 0.0), (0.0, 639.49)]
    return points


def _second_shape() -> list[tuple[float, float]]:
    """M828.7,123.4 L0.15,1000 H500 c276.14,0 500,-223.86 500,-500 h0
    C1000,349.74 933.63,215.06 828.7,123.4 Z"""
    points = [(828.7, 123.4), (0.15, 1000.0), (500.0, 1000.0)]
    points += _cubic_points((500.0, 1000.0), (776.14, 1000.0), (1000.0, 776.14), (1000.0, 500.0))
    points += _cubic_points((1000.0, 500.0), (1000.0, 349.74), (933.63, 215.06), (828.7, 123.4))
    return points


def shapes() -> list[list[tuple[float, float]]]:
    """The logo as a list of polygons in 1000 x 1000 units."""
    return [_first_shape(), _second_shape()]


def draw_on_canvas(canvas: tk.Canvas, size: int, colour: str) -> None:
    """Draw the logo filling a square canvas of the given pixel size."""
    scale = size / SIZE
    canvas.delete("all")
    for polygon in shapes():
        flat = []
        for x, y in polygon:
            flat.extend((x * scale, y * scale))
        canvas.create_polygon(*flat, fill=colour, outline=colour)


def _inside(px: float, py: float, polygon: list[tuple[float, float]]) -> bool:
    """Even-odd point-in-polygon test."""
    inside = False
    count = len(polygon)
    for index in range(count):
        x1, y1 = polygon[index]
        x2, y2 = polygon[(index + 1) % count]
        if (y1 > py) != (y2 > py):
            crossing = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < crossing:
                inside = not inside
    return inside


def icon_photo(master: tk.Misc, size: int, foreground: str) -> tk.PhotoImage:
    """A square icon: the logo in foreground colour, with a transparent background."""
    photo = tk.PhotoImage(master=master, width=size, height=size)
    polygons = shapes()
    for row in range(size):
        py = (row + 0.5) / size * SIZE
        for col in range(size):
            px = (col + 0.5) / size * SIZE
            hit = any(_inside(px, py, polygon) for polygon in polygons)
            if hit:
                photo.put(foreground, to=(col, row))
                photo.transparency_set(col, row, False)
            else:
                photo.transparency_set(col, row, True)
    return photo
