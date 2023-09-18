"""Product models."""
from api import db


class Product(db.Model):
    """Product model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    units = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    order_products = db.relationship("OrderProducts")
    invoice_products = db.relationship("InvoiceProducts")
    purchase_invoice_products = db.relationship("PurchaseInvoiceProducts")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)
