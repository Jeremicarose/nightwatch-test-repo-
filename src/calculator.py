"""Simple calculator module."""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square(n):
    """Return n squared.
    
    BUG: Doesn't handle None!
    """
    return n * n
