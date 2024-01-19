"""Counterparty base apps models."""
from api.app import db


class Discount(db.Model):  # type: ignore
    """Discount model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    rate = db.Column(db.Integer, nullable=False)  # TODO add validator
    counterparties = db.relationship("Counterparty")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Counterparty(db.Model):  # type: ignore
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
    dicounts = db.relationship("Discount", back_populates="counterparties")
    agreements = db.relationship("Agreement")
    orders = db.relationship("Order")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


class Agreement(db.Model):  # type: ignore
    """Agreement model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    counterparty_id = db.Column(
        db.Integer,
        db.ForeignKey("counterparty.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    counterparties = db.relationship("Counterparty", back_populates="agreements")
    invoices = db.relationship("Invoice")
    purchase_invoices = db.relationship("PurchaseInvoice")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.name)


__ALL__ = ("Discount", "Counterparty", "Agreement")
