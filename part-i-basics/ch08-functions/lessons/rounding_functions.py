"""Module for demonstrating rounding strategies"""

import math

def truncate(n: float, dec: int=0) -> float:
    """Truncate a number to a specified number of decimal places"""
    mult = 10 ** dec
    return int(n * mult) / mult


def round_up(n: float, dec: int=0) -> float:
    """Round a number up to a specified number of decimal places"""
    mult = 10 ** dec
    return math.ceil(n * mult) / mult


def round_down(n: float, dec: int=0) -> float:
    """Round a number down to a specified number of decimal places"""
    mult = 10 ** dec
    return math.floor(n * mult) / mult


def round_half_up(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds up)"""
    mult = 10 ** dec
    return math.floor(n * mult + 0.5) / mult


def round_half_down(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places (where 5 rounds down)"""
    mult = 10 ** dec
    return math.ceil(n * mult - 0.5) / mult


def round_half_away_from_zero(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places
       (where 5 rounds up and negative 5 rounds down)"""
    rounded_abs = round_half_up(abs(n), dec)
    return math.copysign(rounded_abs, n)


def round_half_toward_zero(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places
       (where 5 rounds down and negative 5 rounds down)"""
    rounded_abs = round_half_down(abs(n), dec)
    return math.copysign(rounded_abs, n)


def round_half_to_even(n: float, dec: int=0) -> float:
    """Round a number to a specified number of decimal places
       (where 5 rounds up or down to an even number)"""
    return round(n, dec)


def average(numbers: list[float]) -> float:
    """Calculate the average from a list of numbers"""
    return sum(numbers) / len(numbers)
