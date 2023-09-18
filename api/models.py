"""Module for api app models."""
from api import db


class User(db.Model):
    """User model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    orders = db.relationship("Order")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.username)


class Discount(db.Model):
    """Discount model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    rate = db.Column(db.Integer, nullable=False)  # TODO add validator
    counterparties = db.relationship("Counterparty")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Counterparty(db.Model):
    """Counterparty model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    address = db.Column(db.String(255))
    phone_number = db.Column(db.String(30))  # TODO add validator
    discount_id = db.Column(
        db.Integer,
        db.ForeignKey("discount.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True,
    )
    agreements = db.relationship("Agreement")
    orders = db.relationship("Order")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Agreement(db.Model):
    """Agreement model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    counterparty_id = db.Column(
        db.Integer,
        db.ForeignKey("counterparty.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    invoices = db.relationship("Invoice")
    purchase_invoices = db.relationship("PurchaseInvoice")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


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


class Order(db.Model):
    """Order model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("counterparty.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    order_products = db.relationship("OrderProducts")
    invoices = db.relationship("Invoice")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class OrderProducts(db.Model):
    """OrderProducts model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(
        db.Integer,
        db.ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("order.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Order product with id {self.product_id}"


class Invoice(db.Model):
    """Invoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    order_id = db.Column(
        db.Integer,
        db.ForeignKey("order.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, nullable=False)
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
    created_at = db.Column(db.DateTime, nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class PurchaseInvoice(db.Model):
    """PurchaseInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    agreement_id = db.Column(
        db.Integer,
        db.ForeignKey("agreement.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, nullable=False)
    purchase_invoice_products = db.relationship("PurchaseInvoiceProducts")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class PurchaseInvoiceProducts(db.Model):
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
    tax_invoice_products = db.relationship("TaxInvoiceProducts")

    def __repr__(self) -> str:
        """Represent model instance."""
        return f"Purchase invoice product with id {self.product_id}"


class TaxInvoice(db.Model):
    """SaleInvoice model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoice.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    created_at = db.Column(db.DateTime, nullable=False)
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
