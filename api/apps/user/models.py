"""Models for user app."""
from api import db


class User(db.Model):  # type: ignore
    """User model for api app."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=False)
    orders = db.relationship("Order")

    def __repr__(self) -> str:
        """Represent model instance."""
        return str(self.username)
