"""Serivces for order special apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func

from api import Counterparty, Order, OrderProduct, Product, User
from api.common.constants import EARLIEST_DATE, LATEST_DATE


def get_order_registry_data(
    offset: int = 0,
    limit: int = 20,
    date_from: datetime = EARLIEST_DATE,
    date_to: datetime = LATEST_DATE,
) -> Sequence:
    """Get Order registry list."""
    date_from = date_from if date_from else EARLIEST_DATE
    date_to = date_to if date_to else LATEST_DATE
    query = (
        Order.query.with_entities(
            Order.id.label("id"),
            Order.created_at.label("created_at"),
            Order.name.label("order_name"),
            User.username.label("username"),
            Counterparty.name.label("customer"),
            func.sum(
                (OrderProduct.quantity * OrderProduct.price),
            ).label("summ"),
            Product.currency.label("currency"),
        )
        .outerjoin(Order.order_products)
        .join(User)
        .join(Counterparty)
        .outerjoin(Product)
    )
    return (
        query.filter(
            and_(
                Order.created_at > date_from,
                Order.created_at < date_to,
            ),
        )
        .group_by(Order)
        .order_by(Order.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_order_products_by_order_id(order_id: int) -> Sequence:
    """Get Orders products list by base id."""
    return (
        OrderProduct.query.with_entities(
            OrderProduct.id.label("id"),
            OrderProduct.product_id.label("product_id"),
            OrderProduct.quantity.label("quantity"),
            OrderProduct.price.label("price"),
            OrderProduct.order_id.label("order_id"),
            Product.name.label("name"),
            Product.code.label("code"),
            Product.currency.label("currency"),
            Product.units.label("units"),
        )
        .join(Product)
        .filter(OrderProduct.order_id == order_id)
        .all()
    )
