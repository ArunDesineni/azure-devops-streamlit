"""
Unit tests for the calculations module.
Run with: pytest tests/test_calculations.py -v
"""
import pytest
import sys
import os

# Add the 'app' folder to Python path so we can import from utils
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from utils.calculations import (
    add,
    subtract,
    multiply,
    divide,
    calculate_percentage,
)


# ===== Tests for add() =====
class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        """Adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Adding two negative numbers."""
        assert add(-2, -3) == -5

    def test_add_zero(self):
        """Adding zero."""
        assert add(0, 0) == 0
        assert add(5, 0) == 5

    def test_add_decimals(self):
        """Adding decimal numbers."""
        assert add(1.5, 2.5) == 4.0


# ===== Tests for subtract() =====
class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative(self):
        assert subtract(-5, -3) == -2

    def test_subtract_to_zero(self):
        assert subtract(5, 5) == 0


# ===== Tests for multiply() =====
class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(10, 0) == 0

    def test_multiply_negatives(self):
        assert multiply(-3, -4) == 12


# ===== Tests for divide() =====
class TestDivide:
    """Tests for the divide function."""

    def test_divide_normal(self):
        assert divide(10, 2) == 5

    def test_divide_decimal_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self):
        """Dividing by zero should raise ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)


# ===== Tests for calculate_percentage() =====
class TestCalculatePercentage:
    """Tests for the percentage function."""

    def test_percentage_half(self):
        assert calculate_percentage(50, 100) == 50.0

    def test_percentage_full(self):
        assert calculate_percentage(100, 100) == 100.0

    def test_percentage_zero_whole(self):
        """If whole is 0, return 0 (avoid division error)."""
        assert calculate_percentage(50, 0) == 0.0