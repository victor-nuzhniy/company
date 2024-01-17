"""Schemas for purchase apps."""
from api.constants import (
    authorization_parameter,
    code_does_not_exist,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

purchase_invoice_get_schema = {
    "notes": "Get purchase invoice by id.",
    "nickname": "Get purchase invoice.",
    "responseClass": "PurchaseInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


purchase_invoice_put_schema = {
    "notes": "Update purchase invoice data by id.",
    "nickname": "Update purchase invoice.",
    "parameters": [
        {
            "name": "Update purchase invoice",
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
    "notes": "Partially update purchase invoice data by id.",
    "nickname": "Partially update purchase invoice.",
    "parameters": [
        {
            "name": "Partially update purchase invoice",
            "description": "".join((
                "PurchaseInvoice 'name', 'agreement_id' and ",
                "'created_at fields.",
            )),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "P-000012345", "agreement_id": 1, ',
                '"created_at": "2023-09-20"}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": response_message_list,
}


purchase_invoice_delete_schema = {
    "notes": "Delete purchase invoice data by id.",
    "nickname": "Delete purchase invoice.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


purchase_invoice_post_schema = {
    "notes": "Create purchase invoice.",
    "nickname": "Create purchase invoice.",
    "parameters": [
        {
            "name": "Create purchase invoice",
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
    "notes": "Get all purchase invoices.",
    "nickname": "Get all purchase invoices.",
    "responseClass": "PurchaseInvoiceFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


purchase_invoice_product_get_schema = {
    "notes": "Get purchase invoice product by id.",
    "nickname": "Get purchase invoice product.",
    "responseClass": "PurchaseInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


purchase_invoice_product_put_schema = {
    "notes": "Update purchase invoice product data by id.",
    "nickname": "Update purchase invoice product.",
    "parameters": [
        {
            "name": "Update purchase invoice product",
            "description": "".join((
                "PurchaseInvoiceProduct 'product_id', 'quantity', ",
                "'price', 'purchase_invoice_id' and 'products_left' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"product_id": 1, "quantity": 2, "price": 100, ',
                '"purchase_invoice_id": 1, "products_left": 100}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": response_message_list,
}


purchase_invoice_product_patch_schema = {
    "notes": "Partially update purchase invoice product data by id.",
    "nickname": "Partially update purchase invoice product.",
    "parameters": [
        {
            "name": "Partially update purchase invoice product",
            "description": "".join((
                "PurchaseInvoiceProduct 'product_id', 'quantity', ",
                "'price', 'purchase_invoice_id' and 'product_left' fields.",
            )),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"product_id": 1, "quantity": 2, "price": 100, ',
                '"purchase_invoice_id": 1, "products_left": 100}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": response_message_list,
}


purchase_invoice_product_delete_schema = {
    "notes": "Delete purchase invoice product data by id.",
    "nickname": "Delete purchase invoice product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


purchase_invoice_product_post_schema = {
    "notes": "Create purchase invoice product.",
    "nickname": "Create purchase invoice product.",
    "parameters": [
        {
            "name": "Create purchase invoice product",
            "description": "".join((
                "PurchaseInvoiceProduct 'product_id', 'quantity', ",
                "'price', 'purchase_invoice_id' and 'product_left' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"product_id": 1, "quantity": 2, "price": 100, ',
                '"purchase_invoice_id": 1, "products_left": 100}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": response_message_list,
}


purchase_invoice_products_get_schema = {
    "notes": "Get all purchase invoice products.",
    "nickname": "Get all purchase invoice products.",
    "responseClass": "PurchaseInvoiceProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
