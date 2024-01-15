"""Models for sale apps."""
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase

from api import db

BaseModel: DeclarativeBase = db.Model


class SaleInvoice(BaseModel):
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
    invoices = db.relationship("Invoice", back_populates="sale_invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class SaleInvoiceProduct(BaseModel):
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
    products = db.relationship("Product", back_populates="sale_invoice_products")
    sale_invoices = db.relationship(
        "SaleInvoice", back_populates="sale_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Sale_invoice product with id {self.product_id}"
