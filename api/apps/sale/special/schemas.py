"""Schemas for sale special apps."""
from api.common.constants import (
    authorization_parameter,
    code_error,
    code_success,
    small_response_message_list,
)

sale_registry_get_schema = {
    "notes": "Get base registry.",
    "nickname": "Get base registry.",
    "responseClass": "SaleRegistryFields",
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


sale_invoices_products_get_schema = {
    "notes": "Get base base products by base base id.",
    "nickname": "Get base base products by base base id.",
    "responseClass": "SaleInvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


tax_sale_invoices_products_left_get_schema = {
    "notes": "Get base base products by base base id and not in base base.",
    "nickname": "".join(
        (
            "Get base base products by base base id and not in base ",
            "base with tax_invoice_id.",
        ),
    ),
    "responseClass": "SaleInvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


agreement_sale_invoices_get_schema = {
    "notes": "Get all base invoices with agreement id.",
    "nickname": "Get all base invoices with agreement id.",
    "responseClass": "SaleInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
