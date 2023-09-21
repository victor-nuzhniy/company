"""Routes for account apps."""
from flask_restful import Resource


class Account(Resource):
    """Operations with saling process."""

    def post(self):
        """Approve saling and create tax invoice."""
        # args = account_parser.parse_args()
