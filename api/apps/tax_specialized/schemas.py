"""Schemas for tax_specialized apps."""
from api.apps.purchase_specialized.schemas import (
    purchase_invoice_products_left_get_schema,
)
from api.constants import (
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
    "notes": "Get tax invoice registry.",
    "nickname": "Get tax invoice registry.",
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
    "notes": "Get tax invoice products by tax invoice id.",
    "nickname": "Get tax invoice products by tax invoice id.",
    "responseClass": "TaxInvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


tax_invoice_product_with_subtract_post_schema = {
    "notes": "Create tax invoice product with purchase products_left subtraction.",
    "nickname": "Create tax invoice product. with purchase products_left subtraction.",
    "parameters": [
        {
            "name": "".join(
                (
                    "Create tax invoice product with ",
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
            "Delete tax invoice product data by id with",
            " adding purchase products_left.",
        ),
    ),
    "nickname": "Delete tax invoice product with adding purchase products_left.",
    "responseClass": '{"message": "Tax invoice product was successfully deleted."}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


tax_inv_with_purch_add_prod_left_del_schema = {
    "notes": "Delete tax invoice data by id.",
    "nickname": "Delete tax invoice.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}
