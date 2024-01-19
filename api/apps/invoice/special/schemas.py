"""Schemas for invoice special apps."""
from api.common.constants import (
    authorization_parameter,
    code_error,
    code_success,
    small_response_message_list,
)

invoice_registry_get_schema = {
    "notes": "Get base registry.",
    "nickname": "Get base registry.",
    "responseClass": "InvoiceRegistryFields",
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
    "responseMessages": [code_success, code_error],
}


invoices_products_get_schema = {
    "notes": "Get base products by base id.",
    "nickname": "Get base products by base id.",
    "responseClass": "InvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


agreement_invoice_products_get_schema = {
    "notes": "Get all base products with agreement_id.",
    "nickname": "Get all base products with agreement_id.",
    "responseClass": "InvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
