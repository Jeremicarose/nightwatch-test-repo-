"""Simple calculator module with a bug for Nightwatch to fix."""


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
