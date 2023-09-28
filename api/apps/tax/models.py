"""Models for tax apps."""
from sqlalchemy import func

from api import db


class TaxInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sale_invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("sale_invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    tax_invoice_products = db.relationship("TaxInvoiceProduct")
    sale_invoices = db.relationship("SaleInvoice", back_populates="tax_invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class TaxInvoiceProduct(db.Model):
    """TaxInvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    tax_invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("tax_invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    sale_invoice_product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "sale_invoice_product.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
    )
    purchase_invoice_product_id = db.Column(
        db.Integer,
        db.ForeignKey(
            "purchase_invoice_product.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    tax_invoices = db.relationship("TaxInvoice", back_populates="tax_invoice_products")
    sale_invoice_products = db.relationship(
        "SaleInvoiceProducts", back_populates="tax_invoice_products"
    )
    purchase_invoice_products = db.relationship(
        "PurchaseInvoiceProducts", back_populates="tax_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Tax invoice id {self.tax_invoice_id}"
