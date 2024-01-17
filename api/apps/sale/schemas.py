"""Schemas for sale apps."""
from api.constants import (
    authorization_parameter,
    code_does_not_exist,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

sale_invoice_get_schema = {
    "notes": "Get sale invoice by id.",
    "nickname": "Get sale invoice.",
    "responseClass": "SaleInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


sale_invoice_put_schema = {
    "notes": "Update sale invoice data by id.",
    "nickname": "Update sale invoice.",
    "parameters": [
        {
            "name": "Update sale invoice",
            "description": "SaleInvoice 'name' and 'invoice_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "S-000012345", "invoice_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "SaleInvoiceFields",
    "responseMessages": response_message_list,
}


sale_invoice_patch_schema = {
    "notes": "Partially update sale invoice data by id.",
    "nickname": "Partially update sale invoice.",
    "parameters": [
        {
            "name": "Partially update sale invoice",
            "description": "".join(
                (
                    "SaleInvoice 'name', 'invoice_id', 'created_at ",
                    "and 'done' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "S-000012345", "invoice_id": 1, ',
                    '"created_at": "2023-10-01", "done": 0}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "SaleInvoiceFields",
    "responseMessages": response_message_list,
}


sale_invoice_delete_schema = {
    "notes": "Delete sale invoice data by id.",
    "nickname": "Delete sale invoice.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


sale_invoice_post_schema = {
    "notes": "Create sale invoice.",
    "nickname": "Create sale invoice.",
    "parameters": [
        {
            "name": "Create sale invoice",
            "description": "SaleInvoice 'name' and 'invoice_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "S-000012345", "invoice_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "SaleInvoiceFields",
    "responseMessages": response_message_list,
}


sale_invoices_get_schema = {
    "notes": "Get all sale invoices.",
    "nickname": "Get all sale invoices.",
    "responseClass": "SaleInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


sale_invoice_product_get_schema = {
    "notes": "Get sale invoice product by id.",
    "nickname": "Get sale invoice product.",
    "responseClass": "SaleInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


sale_invoice_product_put_schema = {
    "notes": "Update sale invoice product data by id.",
    "nickname": "Update sale invoice product.",
    "parameters": [
        {
            "name": "Update sale invoice product",
            "description": "".join(
                (
                    "SaleInvoiceProduct 'product_id', 'quantity', 'price'",
                    " and 'sale_invoice_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 1, "price": 100, ',
                    '"sale_invoice_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "SaleInvoiceProductFields",
    "responseMessages": response_message_list,
}


sale_invoice_product_patch_schema = {
    "notes": "Partially update sale invoice product data by id.",
    "nickname": "Partially update sale invoice product.",
    "parameters": [
        {
            "name": "Partially update sale invoice product",
            "description": "".join(
                (
                    "SaleInvoiceProduct 'product_id', 'quantity', 'price'",
                    " and 'sale_invoice_id' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"username": "Alex", "email": "a@a.com"}',
        },
    ]
    + authorization_parameter,
    "responseClass": "SaleInvoiceProductFields",
    "responseMessages": response_message_list,
}


sale_invoice_product_delete_schema = {
    "notes": "Delete sale invoice product data by id.",
    "nickname": "Delete sale invoice product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


sale_invoice_product_post_schema = {
    "notes": "Create sale invoice product.",
    "nickname": "Create sale invoice product.",
    "parameters": [
        {
            "name": "Create sale invoice product",
            "description": "".join(
                (
                    "SaleInvoiceProduct 'product_id', 'quantity', 'price'",
                    " and 'sale_invoice_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"username": "Alex", "email": "a@a.com",',
                    ' "password": "111"}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "SaleInvoiceProductFields",
    "responseMessages": response_message_list,
}


sale_invoice_products_get_schema = {
    "notes": "Get all sale invoice products.",
    "nickname": "Get all sale invoice products.",
    "responseClass": "SaleInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
