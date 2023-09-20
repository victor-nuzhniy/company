"""Models for invoice apps."""
from sqlalchemy import func

from api import db
from api.common import AwareDateTime


class Invoice(db.Model):
    """Invoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("order.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(AwareDateTime, default=func.now(), nullable=False)
    paid = db.Column(db.Boolean, default=False)
    agreement_id = db.Column(
        db.Integer,
        db.ForeignKey("agreement.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    invoice_products = db.relationship("InvoiceProducts")
    sale_invoices = db.relationship("SaleInvoice")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class InvoiceProducts(db.Model):
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
    tax_invoice_products = db.relationship("TaxInvoiceProducts")

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Invoice product with id {self.product_id}"


class SaleInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(AwareDateTime, default=func.now(), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)
