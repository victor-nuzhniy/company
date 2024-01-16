"""Utilities for account apps."""
from collections import defaultdict
from typing import Any, Dict, List, Sequence


def get_product_leftovers_on_date(
    purchase_products: Dict, sold_products: Sequence,
) -> List:
    """Subtract quantities in arguments."""
    sold_products_dict = {it.id: it.quantity for it in sold_products}
    for product in purchase_products:
        product["quantity"] -= sold_products_dict.get(product.get("id"), 0)
    return [prod for prod in purchase_products if prod.get("quantity")]


def create_income_products_dict(products: Sequence) -> dict[int, Any]:
    """Create products id: income dict."""
    income_dict: dict[int, Any] = defaultdict(int)
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
    for index in range(len(name)):  # noqa WPS518
        if not name[-index - 1].isnumeric():
            return int(name[-index:])
    return int(name)
