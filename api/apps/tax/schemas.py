"""Schemas for tax apps."""
from api.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

tax_invoice_get_schema = {
    "notes": "Get tax invoice by id.",
    "nickname": "Get tax invoice.",
    "responseClass": "TaxInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


tax_invoice_put_schema = {
    "notes": "Update tax invoice data by id.",
    "nickname": "Update tax invoice.",
    "parameters": [
        {
            "name": "Update tax invoice",
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
    "notes": "Partially update tax invoice data by id.",
    "nickname": "Partially update tax invoice.",
    "parameters": [
        {
            "name": "Partially update tax invoice",
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


tax_invoice_post_schema = {
    "notes": "Create tax invoice.",
    "nickname": "Create tax invoice.",
    "parameters": [
        {
            "name": "Create tax invoice",
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
    "notes": "Get all tax invoices.",
    "nickname": "Get all tax invoices.",
    "responseClass": "TaxInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


tax_invoice_product_get_schema = {
    "notes": "Get tax invoice product by id.",
    "nickname": "Get tax invoice product.",
    "responseClass": "TaxInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


tax_invoice_product_put_schema = {
    "notes": "Update tax invoice product data by id.",
    "nickname": "Update tax invoice product.",
    "parameters": [
        {
            "name": "Update tax invoice product",
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
    "notes": "Partially update tax invoice product data by id.",
    "nickname": "Partially update tax invoice product.",
    "parameters": [
        {
            "name": "Partially update tax invoice product",
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
    "notes": "Delete tax invoice product data by id.",
    "nickname": "Delete tax invoice product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


tax_invoice_product_post_schema = {
    "notes": "Create tax invoice product.",
    "nickname": "Create tax invoice product.",
    "parameters": [
        {
            "name": "Create tax invoice product",
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
    "notes": "Get all tax invoice products.",
    "nickname": "Get all tax invoice products.",
    "responseClass": "TaxInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
