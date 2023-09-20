"""Models for tax apps."""
from sqlalchemy import func

from api import db
from api.common import AwareDateTime


class TaxInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(AwareDateTime, default=func.now(), nullable=False)
    tax_invoice_products = db.relationship("TaxInvoiceProducts")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class TaxInvoiceProducts(db.Model):
    """TaxInvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    tax_invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("tax_invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    invoice_products_id = db.Column(
        db.Integer,
        db.ForeignKey("invoice_products.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    purchase_invoice_products_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "purchase_invoice_products.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Tax invoice id {self.tax_invoice_id}"
