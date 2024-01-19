"""Schemas for tax special apps."""
from api.apps.purchase.special.schemas import purchase_invoice_products_left_get_schema
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_error,
    code_success,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

tax_invoice_product_create_schema = purchase_invoice_products_left_get_schema

tax_registry_get_schema = {
    "notes": "Get base base registry.",
    "nickname": "Get base base registry.",
    "responseClass": "TaxRegistryFields",
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


tax_invoices_products_get_schema = {
    "notes": "Get base base products by base base id.",
    "nickname": "Get base base products by base base id.",
    "responseClass": "TaxInvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


tax_invoice_product_with_subtract_post_schema = {
    "notes": "Create base base base with base products_left subtraction.",
    "nickname": "Create base base base. with base products_left subtraction.",
    "parameters": [
        {
            "name": "".join(
                (
                    "Create base base base with ",
                    "purhcase products_left subtraction.",
                ),
            ),
            "description": "".join(
                (
                    "TaxInvoiceProduct 'tax_invoice_id', ",
                    "'sale_invoice_product_id', 'purchase_invoice_products_id'",
                    " and 'quantity' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"tax_invoice_id": 1, "sale_invoice_product_id": 1, ',
                    '"purchase_invoice_product_id": 1, "quantity": 2}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "TaxInvoiceProductFields",
    "responseMessages": response_message_list,
}


tax_inv_prod_with_add_prod_left_del_schema = {
    "notes": "".join(
        (
            "Delete base base base data by id with",
            " adding base products_left.",
        ),
    ),
    "nickname": "Delete base base base with adding base products_left.",
    "responseClass": '{"message": "Tax base base was successfully deleted."}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


tax_inv_with_purch_add_prod_left_del_schema = {
    "notes": "Delete base base data by id.",
    "nickname": "Delete base base.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}
