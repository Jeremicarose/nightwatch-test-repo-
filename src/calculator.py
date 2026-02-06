"""Simple calculator module."""

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

def cube(n):
    """Return n cubed.
    
    BUG: Crashes on None!
    """
    if n is None:
        raise TypeError("Cannot cube None")
    return n * n * n
