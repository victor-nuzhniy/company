"""Utilities for account apps."""
from collections import defaultdict
from typing import Dict, List, Sequence


def get_product_leftovers_on_date(
    purchase_products: Dict, sold_products: Sequence
) -> List:
    """Subtract quantities in arguments."""
    sold_products_dict = {item.id: item.quantity for item in sold_products}
    for product in purchase_products:
        product["quantity"] -= sold_products_dict.get(product.get("id"), 0)
    result = [product for product in purchase_products if product.get("quantity")]
    return result


def create_income_products_dict(products: Sequence):
    """Create products id: income dict."""
    income_dict = defaultdict(int)
    for product in products:
        income_dict[product.product_id] += product.quantity * (
            product.sale_price - product.purchase_price
        )
    return income_dict


def add_income_to_products(income_dict: Dict, products: List[Dict]) -> List[Dict]:
    """Add income data to products list."""
    for product in products:
        product["income"] = income_dict.get(product.get("id"))
    return products


def get_last_string_digits_number(name: str) -> int:
    """Get last possible digits from a str."""
    for i in range(len(name)):
        if not name[-i - 1].isnumeric():
            return int(name[-i:])
    return int(name)
