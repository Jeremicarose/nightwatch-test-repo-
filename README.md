# Nightwatch Test Repo

A simple Python calculator with a **deliberate bug** for testing Nightwatch self-healing.

## The Bug

`src/calculator.py` has a `divide()` function that doesn't handle division by zero.

The test `test_divide_by_zero` expects a `ValueError` but gets `ZeroDivisionError`.

## Expected Fix

Nightwatch should detect the CI failure and create a PR that adds:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

 
