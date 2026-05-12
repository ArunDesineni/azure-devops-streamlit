"""
Generate sample data for demo purposes.
"""
import random
from datetime import datetime, timedelta


def generate_sales_data(days: int = 30) -> list:
    """Generate random sales data for the last N days."""
    data = []
    today = datetime.now()
    
    for i in range(days):
        date = today - timedelta(days=i)
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "sales": random.randint(1000, 5000),
            "orders": random.randint(10, 100),
        })
    
    return sorted(data, key=lambda x: x["date"])


def get_top_products() -> list:
    """Return a list of top-selling products."""
    return [
        {"product": "Laptop", "units": 150, "revenue": 150000},
        {"product": "Phone", "units": 300, "revenue": 240000},
        {"product": "Headphones", "units": 500, "revenue": 75000},
        {"product": "Tablet", "units": 100, "revenue": 80000},
        {"product": "Watch", "units": 200, "revenue": 60000},
    ]