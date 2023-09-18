"""Models for order apps."""
from api import db


class Order(db.Model):
    """Order model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("counterparty.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    order_products = db.relationship("OrderProducts")
    invoices = db.relationship("Invoice")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class OrderProducts(db.Model):
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

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Order product with id {self.product_id}"
