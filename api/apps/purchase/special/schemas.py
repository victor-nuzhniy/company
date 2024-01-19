"""Schemas for purchase special apps."""
from api.common.constants import (
    authorization_parameter,
    code_error,
    code_success,
    small_response_message_list,
)

purchase_registry_get_schema = {
    "notes": "Get base registry.",
    "nickname": "Get base registry.",
    "responseClass": "PurchaseRegistryFields",
    "parameters": authorization_parameter
    + [
        {
            "name": "offset",
            "description": "Query parameters offset",
            "required": False,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "query",
            "defaultValue": 0,
        },
        {
            "name": "limit",
            "description": "Query parameters limit",
            "required": False,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "query",
            "defaultValue": 20,
        },
        {
            "name": "date_from",
            "description": "Query parameters limit",
            "required": False,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "query",
            "defaultValue": "2020-01-01",
        },
        {
            "name": "date_to",
            "description": "Query parameters limit",
            "required": False,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "query",
            "defaultValue": "2024-01-01",
        },
    ],
    "responseMessages": [
        code_success,
        code_error,
    ],
}


purchase_invoices_products_get_schema = {
    "notes": "Get base base products by base base id.",
    "nickname": "Get base base products by base base id.",
    "responseClass": "PurchaseInvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


purchase_invoice_products_left_get_schema = {
    "notes": "Get base base products with products left > 0 and base id.",
    "nickname": "Get base base products with products left > 0 and base id.",
    "responseClass": "PurchaseInvoiceProductsLeftFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
