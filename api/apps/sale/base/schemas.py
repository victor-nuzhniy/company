"""Schemas for sale base apps."""
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

sale_invoice_get_schema = {
    "notes": "Get base base by id.",
    "nickname": "Get base base.",
    "responseClass": "SaleInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


sale_invoice_put_schema = {
    "notes": "Update base base data by id.",
    "nickname": "Update base base.",
    "parameters": [
        {
            "name": "Update base base",
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
    "notes": "Partially update base base data by id.",
    "nickname": "Partially update base base.",
    "parameters": [
        {
            "name": "Partially update base base",
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


sale_invoice_post_schema = {
    "notes": "Create base base.",
    "nickname": "Create base base.",
    "parameters": [
        {
            "name": "Create base base",
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
    "notes": "Get all base invoices.",
    "nickname": "Get all base invoices.",
    "responseClass": "SaleInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


sale_invoice_product_get_schema = {
    "notes": "Get base base base by id.",
    "nickname": "Get base base base.",
    "responseClass": "SaleInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


sale_invoice_product_put_schema = {
    "notes": "Update base base base data by id.",
    "nickname": "Update base base base.",
    "parameters": [
        {
            "name": "Update base base base",
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
    "notes": "Partially update base base base data by id.",
    "nickname": "Partially update base base base.",
    "parameters": [
        {
            "name": "Partially update base base base",
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
    "notes": "Delete base base base data by id.",
    "nickname": "Delete base base base.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


sale_invoice_product_post_schema = {
    "notes": "Create base base base.",
    "nickname": "Create base base base.",
    "parameters": [
        {
            "name": "Create base base base",
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
    "notes": "Get all base base products.",
    "nickname": "Get all base base products.",
    "responseClass": "SaleInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
