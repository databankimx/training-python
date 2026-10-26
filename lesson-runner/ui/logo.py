"""DataBank IMX logo, drawn from the two SVG paths in the WPF MainWindow.xaml.

The paths are converted to polygons in a 1000 x 1000 coordinate space. The icons
module draws them with Qt. Nothing is read from an image file.
"""

from __future__ import annotations

import math

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

    points: list[tuple[float, float]] = []
    for step in range(1, ARC_STEPS + 1):
        theta = theta1 + delta * step / ARC_STEPS
        points.append((cx + rx * math.cos(theta), cy + ry * math.sin(theta)))
    return points


def _cubic_points(p0: tuple[float, float], p1: tuple[float, float],
                  p2: tuple[float, float], p3: tuple[float, float]) -> list[tuple[float, float]]:
    """Points along a cubic Bezier curve, start excluded."""
    points: list[tuple[float, float]] = []
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
