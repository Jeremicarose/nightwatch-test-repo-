"""Calculator."""

def add(a, b):
    return a + b

def invert(n):
    """Return 1/n. BUG: No zero check!"""
    if n == 0:
        raise ValueError("Cannot invert zero")
    return 1 / n
