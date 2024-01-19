"""Schemas for tax base apps."""
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

tax_invoice_get_schema = {
    "notes": "Get base base by id.",
    "nickname": "Get base base.",
    "responseClass": "TaxInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


tax_invoice_put_schema = {
    "notes": "Update base base data by id.",
    "nickname": "Update base base.",
    "parameters": [
        {
            "name": "Update base base",
            "description": "TaxInvoice 'name' and 'sale_invoice_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "T-000012345", "sale_invoice_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "TaxInvoiceFields",
    "responseMessages": response_message_list,
}


tax_invoice_patch_schema = {
    "notes": "Partially update base base data by id.",
    "nickname": "Partially update base base.",
    "parameters": [
        {
            "name": "Partially update base base",
            "description": "".join(
                (
                    "TaxInvoice 'name', 'sale_invoice_id' and ",
                    "'created_at' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "T-000012345", "sale_invoice_id": 1,',
                    ' "created_at": "2023-10-01"}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "TaxInvoiceFields",
    "responseMessages": response_message_list,
}


tax_invoice_delete_schema = {
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


tax_invoice_post_schema = {
    "notes": "Create base base.",
    "nickname": "Create base base.",
    "parameters": [
        {
            "name": "Create base base",
            "description": "TaxInvoice 'name' and 'sale_invoice_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "T-000012345", "sale_invoice_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "TaxInvoiceFields",
    "responseMessages": response_message_list,
}


tax_invoices_get_schema = {
    "notes": "Get all base invoices.",
    "nickname": "Get all base invoices.",
    "responseClass": "TaxInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


tax_invoice_product_get_schema = {
    "notes": "Get base base base by id.",
    "nickname": "Get base base base.",
    "responseClass": "TaxInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


tax_invoice_product_put_schema = {
    "notes": "Update base base base data by id.",
    "nickname": "Update base base base.",
    "parameters": [
        {
            "name": "Update base base base",
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


tax_invoice_product_patch_schema = {
    "notes": "Partially update base base base data by id.",
    "nickname": "Partially update base base base.",
    "parameters": [
        {
            "name": "Partially update base base base",
            "description": "".join(
                (
                    "TaxInvoiceProduct 'tax_invoice_id', ",
                    "'sale_invoice_product_id', 'purchase_invoice_products_id'",
                    " and 'quantity' fields.",
                ),
            ),
            "required": False,
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


tax_invoice_product_delete_schema = {
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


tax_invoice_product_post_schema = {
    "notes": "Create base base base.",
    "nickname": "Create base base base.",
    "parameters": [
        {
            "name": "Create base base base",
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


tax_invoice_products_get_schema = {
    "notes": "Get all base base products.",
    "nickname": "Get all base base products.",
    "responseClass": "TaxInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
