"""Models for purchase apps."""
from sqlalchemy import func

from api import db


class PurchaseInvoice(db.Model):
    """PurchaseInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    agreement_id = db.Column(
        db.Integer,
        db.ForeignKey("agreement.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    purchase_invoice_products = db.relationship("PurchaseInvoiceProduct")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class PurchaseInvoiceProduct(db.Model):
    """PurchaseInvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    purchase_invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("purchase_invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    products_left = db.Column(db.Integer, nullable=False)
    tax_invoice_products = db.relationship("TaxInvoiceProduct")

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Purchase invoice product with id {self.product_id}"
