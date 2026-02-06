"""Simple calculator."""

def add(a, b):
    return a + b

def decrement(n):
    """Subtract 1 from n. BUG: Crashes on None!"""
    if n is None:
        raise TypeError("Cannot decrement None")
    return n - 1
