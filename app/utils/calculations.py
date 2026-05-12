"""
Reusable calculation functions.
These will be tested in Stage 4!
"""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises error if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def calculate_percentage(part: float, whole: float) -> float:
    """Calculate what percentage 'part' is of 'whole'."""
    if whole == 0:
        return 0.0
    return (part / whole) * 100