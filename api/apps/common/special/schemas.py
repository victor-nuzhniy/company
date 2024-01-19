"""Schemas for common special apps."""
from api.common.constants import (
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
