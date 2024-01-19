"""Schemas for purchase base apps."""
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

purchase_invoice_get_schema = {
    "notes": "Get base base by id.",
    "nickname": "Get base base.",
    "responseClass": "PurchaseInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


purchase_invoice_put_schema = {
    "notes": "Update base base data by id.",
    "nickname": "Update base base.",
    "parameters": [
        {
            "name": "Update base base",
            "description": "PurchaseInvoice 'name' and 'agreement_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "P-000012345", "agreement_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": response_message_list,
}


purchase_invoice_patch_schema = {
    "notes": "Partially update base base data by id.",
    "nickname": "Partially update base base.",
    "parameters": [
        {
            "name": "Partially update base base",
            "description": "".join(
                (
                    "PurchaseInvoice 'name', 'agreement_id' and ",
                    "'created_at fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "P-000012345", "agreement_id": 1, ',
                    '"created_at": "2023-09-20"}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": response_message_list,
}


purchase_invoice_delete_schema = {
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


purchase_invoice_post_schema = {
    "notes": "Create base base.",
    "nickname": "Create base base.",
    "parameters": [
        {
            "name": "Create base base",
            "description": "PurchaseInvoice 'name' and 'agreement_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "P-000012345", "agreement_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": response_message_list,
}


purchase_invoices_get_schema = {
    "notes": "Get all base invoices.",
    "nickname": "Get all base invoices.",
    "responseClass": "PurchaseInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


purchase_invoice_product_get_schema = {
    "notes": "Get base base base by id.",
    "nickname": "Get base base base.",
    "responseClass": "PurchaseInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


purchase_invoice_product_put_schema = {
    "notes": "Update base base base data by id.",
    "nickname": "Update base base base.",
    "parameters": [
        {
            "name": "Update base base base",
            "description": "".join(
                (
                    "PurchaseInvoiceProduct 'product_id', 'quantity', ",
                    "'price', 'purchase_invoice_id' and 'products_left' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, "price": 100, ',
                    '"purchase_invoice_id": 1, "products_left": 100}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": response_message_list,
}


purchase_invoice_product_patch_schema = {
    "notes": "Partially update base base base data by id.",
    "nickname": "Partially update base base base.",
    "parameters": [
        {
            "name": "Partially update base base base",
            "description": "".join(
                (
                    "PurchaseInvoiceProduct 'product_id', 'quantity', ",
                    "'price', 'purchase_invoice_id' and 'product_left' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, "price": 100, ',
                    '"purchase_invoice_id": 1, "products_left": 100}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": response_message_list,
}


purchase_invoice_product_delete_schema = {
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


purchase_invoice_product_post_schema = {
    "notes": "Create base base base.",
    "nickname": "Create base base base.",
    "parameters": [
        {
            "name": "Create base base base",
            "description": "".join(
                (
                    "PurchaseInvoiceProduct 'product_id', 'quantity', ",
                    "'price', 'purchase_invoice_id' and 'product_left' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, "price": 100, ',
                    '"purchase_invoice_id": 1, "products_left": 100}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": response_message_list,
}


purchase_invoice_products_get_schema = {
    "notes": "Get all base base products.",
    "nickname": "Get all base base products.",
    "responseClass": "PurchaseInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
