"""Models for order apps."""
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeMeta

from api import db

BaseModel: DeclarativeMeta = db.Model


class Order(BaseModel):
    """Order model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("counterparty.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    order_products = db.relationship("OrderProduct")
    invoices = db.relationship("Invoice", back_populates="orders")
    users = db.relationship("User", back_populates="orders")
    customers = db.relationship("Counterparty", back_populates="orders")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class OrderProduct(BaseModel):
    """OrderProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("order.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    products = db.relationship("Product", back_populates="order_products")
    orders = db.relationship("Order", back_populates="order_products")

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Order product with id {self.product_id}"
