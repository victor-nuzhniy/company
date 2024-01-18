"""Serivces for order_specialized apps."""
from datetime import datetime
from typing import Sequence

from sqlalchemy import and_, func

from api.apps.counterparty import models as counterparty_models
from api.apps.order import models as order_models
from api.apps.product import models as product_models
from api.apps.user import models as user_models
from api.constants import EARLIEST_DATE, LATEST_DATE


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
        order_models.Order.query.with_entities(
            order_models.Order.id.label("id"),
            order_models.Order.created_at.label("created_at"),
            order_models.Order.name.label("order_name"),
            user_models.User.username.label("username"),
            counterparty_models.Counterparty.name.label("customer"),
            func.sum(
                (order_models.OrderProduct.quantity * order_models.OrderProduct.price),
            ).label("summ"),
            product_models.Product.currency.label("currency"),
        )
        .outerjoin(order_models.Order.order_products)
        .join(user_models.User)
        .join(counterparty_models.Counterparty)
        .outerjoin(product_models.Product)
    )
    return (
        query.filter(
            and_(
                order_models.Order.created_at > date_from,
                order_models.Order.created_at < date_to,
            ),
        )
        .group_by(order_models.Order)
        .order_by(order_models.Order.id.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_order_products_by_order_id(order_id: int) -> Sequence:
    """Get Orders products list by order id."""
    return (
        order_models.OrderProduct.query.with_entities(
            order_models.OrderProduct.id.label("id"),
            order_models.OrderProduct.product_id.label("product_id"),
            order_models.OrderProduct.quantity.label("quantity"),
            order_models.OrderProduct.price.label("price"),
            order_models.OrderProduct.order_id.label("order_id"),
            product_models.Product.name.label("name"),
            product_models.Product.code.label("code"),
            product_models.Product.currency.label("currency"),
            product_models.Product.units.label("units"),
        )
        .join(product_models.Product)
        .filter(order_models.OrderProduct.order_id == order_id)
        .all()
    )
