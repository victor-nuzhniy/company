"""Schemas for common_services apps."""
from api.constants import (
    authorization_parameter,
    code_error,
    code_success,
    code_unauthorized,
)

name_number_schema = {
    "notes": "Get number for document name based on last name number.",
    "nickname": "Get number for document name based on last name number.",
    "parameters": authorization_parameter,
    "responseClass": "NameNumber",
    "responseMessages": [
        code_success,
        code_error,
        code_unauthorized,
        {
            "code": 409,
            "message": "".join(
                (
                    "'model_name' is not in Order, Invoice,",
                    " PurchaseInvoice, SaleInvoice, TaxInvoice models.",
                ),
            ),
        },
    ],
}
