"""Schemas for invoice base apps."""
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

invoice_get_schema = {
    "notes": "Get base by id.",
    "nickname": "Get base.",
    "responseClass": "InvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


invoice_put_schema = {
    "notes": "Update base data by id.",
    "nickname": "Update base.",
    "parameters": [
        {
            "name": "Update base",
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
    "notes": "Partially update base data by id.",
    "nickname": "Partially update base.",
    "parameters": [
        {
            "name": "Partially update base",
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
    "notes": "Delete base data by id.",
    "nickname": "Delete base.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


invoice_post_schema = {
    "notes": "Create base.",
    "nickname": "Create base.",
    "parameters": [
        {
            "name": "Create base",
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
    "notes": "Get base base by id.",
    "nickname": "Get base base.",
    "responseClass": "InvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


invoice_product_put_schema = {
    "notes": "Update base base data by id.",
    "nickname": "Update base base.",
    "parameters": [
        {
            "name": "Update base base",
            "description": "".join(
                (
                    "Invoice base 'product_id', ",
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
    "notes": "Partially update base base data by id.",
    "nickname": "Partially update base base.",
    "parameters": [
        {
            "name": "Partially update base base",
            "description": "".join(
                (
                    "Invoice base 'product_id', ",
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


invoice_product_post_schema = {
    "notes": "Create base base.",
    "nickname": "Create base base.",
    "parameters": [
        {
            "name": "Create base base",
            "description": "".join(
                (
                    "Invoice base 'product_id', ",
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
    "notes": "Get all base products.",
    "nickname": "Get all base products.",
    "responseClass": "InvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
