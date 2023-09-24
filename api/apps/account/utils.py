"""Utilities for account apps."""
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
