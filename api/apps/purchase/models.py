"""Models for purchase apps."""
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeMeta

from api import db

BaseModel: DeclarativeMeta = db.Model


class PurchaseInvoice(BaseModel):
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
    agreements = db.relationship("Agreement", back_populates="purchase_invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class PurchaseInvoiceProduct(BaseModel):
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
    products = db.relationship("Product", back_populates="purchase_invoice_products")
    purchase_invoices = db.relationship(
        "PurchaseInvoice", back_populates="purchase_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Purchase invoice product with id {self.product_id}"
