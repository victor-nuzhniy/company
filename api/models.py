"""Module for api app models."""
from api import db


class User(db.Model):
    """User model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60))
    is_admin = db.Column(db.Boolean, default=False)
    orders = db.relationship("Order", backref="orders")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.username)


class Discount(db.Model):
    """Discount model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    rate = db.Column(db.Integer)  # TODO add validator
    counterparties = db.relationship("CounterParty", backref="counterparties")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class CounterParty(db.Model):
    """CounterParty model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(30))  # TODO add validator
    discount_id = db.Column(db.Integer, db.ForeignKey("discount.id"), nullable=True)
    agreements = db.relationship("Agreement", backref="agreements")
    orders = db.relationship("Order", backref="orders")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Agreement(db.Model):
    """Agreement model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    counterparty_id = db.Column(db.Integer, db.ForeignKey("counterparty.id"))
    invoices = db.relationship("Invoice", backref="invoices")
    purchase_invoices = db.relationship("PurchaseInvoice", backref="purchase_invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Product(db.Model):
    """Product model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    code = db.Column(db.String(100), unique=True)
    units = db.Column(db.String(100))
    price = db.Column(db.Integer)
    order_products = db.relationship("OrderProducts", backref="order_products")
    invoice_products = db.relationship("InvoiceProducts", backref="invoice_products")
    purchase_invoice_products = db.relationship(
        "PurchaseInvoiceProducts", backref="purchase_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Order(db.Model):
    """Order model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(100), unique=True)
    created_at = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey("counterparty.id"))
    order_products = db.relationship("Order", backref="order_products")
    invoices = db.relationship("Invoice", backref="invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class OrderProducts(db.Model):
    """OrderProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Order product with id {self.product_id}"


class Invoice(db.Model):
    """Invoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    created_at = db.Column(db.DateTime)
    paid = db.Column(db.Boolean)
    agreement_id = db.Column(db.Integer, db.ForeignKey("agreement.id"))
    invoice_products = db.relationship("InvoiceProducts", backref="invoice_products")
    sale_invoices = db.relationship("SaleInvoice", backref="sale_invoices")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class InvoiceProducts(db.Model):
    """InvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))
    tax_invoice_products = db.relationship(
        "TaxInvoiceProducts", backref="tax_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Invoice product with id {self.product_id}"


class SaleInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))
    created_at = db.Column(db.DateTime)
    done = db.Column(db.Boolean)

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class PurchaseInvoice(db.Model):
    """PurchaseInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    agreement_id = db.Column(db.Integer, db.ForeignKey("agreement.id"))
    created_at = db.Column(db.DateTime)
    purchase_invoice_products = db.relationship(
        "PurchaseInvoiceProducts", backref="purchase_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class PurchaseInvoiceProducts(db.Model):
    """PurchaseInvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    purchase_invoice_id = db.Column(db.Integer, db.ForeignKey("purchase_invoice.id"))
    products_left = db.Column(db.Integer)
    tax_invoice_products = db.relationship(
        "TaxInvoiceProducts", backref="tax_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Purchase invoice product with id {self.product_id}"


class TaxInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    invoice_id = db.Column(db.Integer, db.ForeignKey("invoice.id"))
    created_at = db.Column(db.DateTime)
    tax_invoice_products = db.relationship(
        "TaxInvoiceProducts", backref="tax_invoice_products"
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class TaxInvoiceProducts(db.Model):
    """TaxInvoiceProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    tax_invoice_id = db.Column(db.Integer, db.ForeignKey("tax_invoice.id"))
    invoice_products_id = db.Column(db.Integer, db.ForeignKey("invoice_products.id"))
    purchase_invoice_products_id = db.Column(
        db.Integer, db.ForeignKey("purchase_invoice_products.id")
    )
    quantity = db.Column(db.Integer)

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Tax invoice id {self.tax_invoice_id}"
