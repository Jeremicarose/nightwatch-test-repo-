"""Simple calculator module with a bug for Nightwatch to fix."""

import math


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b.

    BUG: Missing zero division check - Nightwatch should fix this!
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    """Raise base to the power of exponent.

    BUG: Doesn't handle None values - will crash!
    """
    if base is None:
        return None
    return base ** exponent


def square_root(n):
    """Calculate the square root of n.

    BUG: Doesn't handle negative numbers - will crash with ValueError!
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(n)



def double(n):
    """Double a number.
    
    BUG: Doesn't handle None!
    """
    return n * 2
