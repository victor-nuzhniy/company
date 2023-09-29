"""Schemas for tax apps."""


tax_invoice_get_schema = {
    "notes": "Get tax invoice by id.",
    "nickname": "Get tax invoice.",
    "responseClass": "TaxInvoiceFields",
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
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
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "TaxInvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoice_patch_schema = {
    "notes": "Partially update tax invoice data by id.",
    "nickname": "Partially update tax invoice.",
    "parameters": [
        {
            "name": "Partially update tax invoice",
            "description": "TaxInvoice 'name', 'sale_invoice_id' and "
            "'created_at' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "T-000012345", "sale_invoice_id": 1,'
            ' "created_at": "2023-10-01"}',
        },
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "TaxInvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoice_delete_schema = {
    "notes": "Delete tax invoice data by id.",
    "nickname": "Delete tax invoice.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
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
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "TaxInvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoices_get_schema = {
    "notes": "Get all tax invoices.",
    "nickname": "Get all tax invoices.",
    "responseClass": "TaxInvoiceFields",
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


tax_invoice_product_get_schema = {
    "notes": "Get tax invoice product by id.",
    "nickname": "Get tax invoice product.",
    "responseClass": "TaxInvoiceProductFields",
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoice_product_put_schema = {
    "notes": "Update tax invoice product data by id.",
    "nickname": "Update tax invoice product.",
    "parameters": [
        {
            "name": "Update tax invoice product",
            "description": "TaxInvoiceProduct 'tax_invoice_id', "
            "'sale_invoice_product_id', 'purchase_invoice_products_id'"
            " and 'quantity' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"tax_invoice_id": 1, "sale_invoice_products_id": 1, '
            '"purchase_invoice_products_id": 1, "quantity": 2}',
        },
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "TaxInvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoice_product_patch_schema = {
    "notes": "Partially update tax invoice product data by id.",
    "nickname": "Partially update tax invoice product.",
    "parameters": [
        {
            "name": "Partially update tax invoice product",
            "description": "TaxInvoiceProduct 'tax_invoice_id', "
            "'sale_invoice_product_id', 'purchase_invoice_products_id'"
            " and 'quantity' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"tax_invoice_id": 1, "sale_invoice_products_id": 1, '
            '"purchase_invoice_products_id": 1, "quantity": 2}',
        },
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "TaxInvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoice_product_delete_schema = {
    "notes": "Delete tax invoice product data by id.",
    "nickname": "Delete tax invoice product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


tax_invoice_product_post_schema = {
    "notes": "Create tax invoice product.",
    "nickname": "Create tax invoice product.",
    "parameters": [
        {
            "name": "Create tax invoice product",
            "description": "TaxInvoiceProduct 'tax_invoice_id', "
            "'sale_invoice_product_id', 'purchase_invoice_products_id'"
            " and 'quantity' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"tax_invoice_id": 1, "sale_invoice_products_id": 1, '
            '"purchase_invoice_products_id": 1, "quantity": 2}',
        },
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "TaxInvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


tax_invoice_products_get_schema = {
    "notes": "Get all tax invoice products.",
    "nickname": "Get all tax invoice products.",
    "responseClass": "TaxInvoiceProductFields",
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
