"""Schemas for invoice apps."""
from api.constants import (
    authorization_parameter,
    code_does_not_exist,
    code_error,
    code_success,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

invoice_get_schema = {
    "notes": "Get invoice by id.",
    "nickname": "Get invoice.",
    "responseClass": "InvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


invoice_put_schema = {
    "notes": "Update invoice data by id.",
    "nickname": "Update invoice.",
    "parameters": [
        {
            "name": "Update invoice",
            "description": "Invoice 'name', 'order_id' and 'agreement_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "I-00357", "order_id": 1, "agreement_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "InvoiceFields",
    "responseMessages": response_message_list,
}


invoice_patch_schema = {
    "notes": "Partially update invoice data by id.",
    "nickname": "Partially update invoice.",
    "parameters": [
        {
            "name": "Partially update invoice",
            "description": "".join(
                (
                    "Invoice 'name', 'order_id', 'created_at' ",
                    "and 'agreement_id' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "I-00357", "order_id": 1, ',
                    '"created_at": "2023-10-01", "agreement_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "InvoiceFields",
    "responseMessages": response_message_list,
}


invoice_delete_schema = {
    "notes": "Delete invoice data by id.",
    "nickname": "Delete invoice.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


invoice_post_schema = {
    "notes": "Create invoice.",
    "nickname": "Create invoice.",
    "parameters": [
        {
            "name": "Create invoice",
            "description": "Invoice 'name', 'order_id' and 'agreement_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "I-00357", "order_id": 1, "agreement_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "InvoiceFields",
    "responseMessages": response_message_list,
}


invoices_get_schema = {
    "notes": "Get all invoices.",
    "nickname": "Get all invoices.",
    "responseClass": "InvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


invoice_product_get_schema = {
    "notes": "Get invoice product by id.",
    "nickname": "Get invoice product.",
    "responseClass": "InvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


invoice_product_put_schema = {
    "notes": "Update invoice product data by id.",
    "nickname": "Update invoice product.",
    "parameters": [
        {
            "name": "Update invoice product",
            "description": "".join(
                (
                    "Invoice product 'product_id', ",
                    "'quantity', 'price' and 'invoice_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, ',
                    '"price": 100, "invoice_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "InvoiceProductFields",
    "responseMessages": response_message_list,
}


invoice_product_patch_schema = {
    "notes": "Partially update invoice product data by id.",
    "nickname": "Partially update invoice product.",
    "parameters": [
        {
            "name": "Partially update invoice product",
            "description": "".join(
                (
                    "Invoice product 'product_id', ",
                    "'quantity', 'price' and 'invoice_id' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, ',
                    '"price": 100, "invoice_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "InvoiceProductFields",
    "responseMessages": response_message_list,
}


invoice_product_delete_schema = {
    "notes": "Delete invoice product data by id.",
    "nickname": "Delete invoice product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


invoice_product_post_schema = {
    "notes": "Create invoice product.",
    "nickname": "Create invoice product.",
    "parameters": [
        {
            "name": "Create invoice product",
            "description": "".join(
                (
                    "Invoice product 'product_id', ",
                    "'quantity', 'price' and 'invoice_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, ',
                    '"price": 100, "invoice_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "InvoiceProductFields",
    "responseMessages": response_message_list,
}


invoice_products_get_schema = {
    "notes": "Get all invoice products.",
    "nickname": "Get all invoice products.",
    "responseClass": "InvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


invoice_registry_get_schema = {
    "notes": "Get invoice registry.",
    "nickname": "Get invoice registry.",
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
    "notes": "Get invoice products by invoice id.",
    "nickname": "Get invoice products by invoice id.",
    "responseClass": "InvoicesProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


agreement_invoice_products_get_schema = {
    "notes": "Get all invoice products with agreement_id.",
    "nickname": "Get all invoice products with agreement_id.",
    "responseClass": "InvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
