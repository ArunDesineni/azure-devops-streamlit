"""
Unit tests for the data_generator module.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from utils.data_generator import generate_sales_data, get_top_products


class TestGenerateSalesData:
    """Tests for generate_sales_data function."""

    def test_default_returns_30_days(self):
        """By default, should return 30 days of data."""
        data = generate_sales_data()
        assert len(data) == 30

    def test_custom_days(self):
        """Should respect custom day count."""
        data = generate_sales_data(days=7)
        assert len(data) == 7

    def test_data_has_required_fields(self):
        """Each entry must have date, sales, and orders."""
        data = generate_sales_data(days=5)
        for entry in data:
            assert "date" in entry
            assert "sales" in entry
            assert "orders" in entry

    def test_sales_are_in_expected_range(self):
        """Sales values should be between 1000 and 5000."""
        data = generate_sales_data(days=10)
        for entry in data:
            assert 1000 <= entry["sales"] <= 5000

    def test_data_is_sorted_by_date(self):
        """Data should be returned in chronological order."""
        data = generate_sales_data(days=10)
        dates = [entry["date"] for entry in data]
        assert dates == sorted(dates)


class TestGetTopProducts:
    """Tests for get_top_products function."""

    def test_returns_list(self):
        """Should return a list."""
        products = get_top_products()
        assert isinstance(products, list)

    def test_has_five_products(self):
        """Should return exactly 5 products."""
        products = get_top_products()
        assert len(products) == 5

    def test_each_product_has_required_fields(self):
        """Each product must have product, units, revenue."""
        products = get_top_products()
        for p in products:
            assert "product" in p
            assert "units" in p
            assert "revenue" in p

    def test_revenues_are_positive(self):
        """All revenue values must be positive."""
        products = get_top_products()
        for p in products:
            assert p["revenue"] > 0