"""Models for invoice apps."""
from sqlalchemy import func

from api import db


class Invoice(db.Model):
    """Invoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("order.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    paid = db.Column(db.Boolean, default=False)
    agreement_id = db.Column(
        db.Integer,
        db.ForeignKey("agreement.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    agreements = db.relationship("Agreement", back_populates="invoices")
    orders = db.relationship("Order", back_populates="invoices")
    invoice_products = db.relationship("InvoiceProduct", back_populates="invoices")
    sale_invoices = db.relationship("SaleInvoice", back_populates="invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class InvoiceProduct(db.Model):
    """InvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    products = db.relationship("Product", back_populates="invoice_products")
    invoices = db.relationship("Invoice", back_populates="invoice_products")

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Invoice product with id {self.product_id}"
