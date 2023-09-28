"""Product models."""
from api import db


class ProductType(db.Model):
    """ProductType model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship("Product")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Product(db.Model):
    """Product model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    units = db.Column(db.String(100), nullable=False)
    currency = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    product_type_id = db.Column(
        db.Integer,
        db.ForeignKey("product_type.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    order_products = db.relationship("OrderProduct")
    invoice_products = db.relationship("InvoiceProduct")
    sale_invoice_products = db.relationship("SaleInvoiceProduct")
    purchase_invoice_products = db.relationship("PurchaseInvoiceProduct")
    product_types = db.relationship("ProductType", back_populates="products")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)
