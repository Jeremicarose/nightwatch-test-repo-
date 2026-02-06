"""Calculator."""

def add(a, b):
    return a + b

def double(n):
    """Double n. BUG: Crashes on None!"""
    if n is None:
        raise TypeError("Cannot double None")
    return n * 2
