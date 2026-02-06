"""Calculator."""

def add(a, b):
    return a + b

def square(n):
    """Square n. BUG: Crashes on None!"""
    if n is None:
        raise TypeError("Cannot square None")
    return n * n
