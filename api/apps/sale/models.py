"""Models for sale apps."""
from sqlalchemy import func

from api import db


class SaleInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    done = db.Column(db.Boolean, default=False)
    tax_invoices = db.relationship("TaxInvoice")
    sale_invoice_products = db.relationship("SaleInvoiceProduct")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class SaleInvoiceProduct(db.Model):
    """InvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    sale_invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("sale_invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    tax_invoice_products = db.relationship("TaxInvoiceProduct")

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Sale_invoice product with id {self.product_id}"
