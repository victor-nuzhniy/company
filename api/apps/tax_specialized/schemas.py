"""Schemas for tax_specialized apps."""




tax_registry_get_schema = {
    "notes": "Get tax invoice registry.",
    "nickname": "Get tax invoice registry.",
    "responseClass": "TaxRegistryFields",
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
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
    ],
}


tax_invoices_products_get_schema = {
    "notes": "Get tax invoice products by tax invoice id.",
    "nickname": "Get tax invoice products by tax invoice id.",
    "responseClass": "TaxInvoicesProductsFields",
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
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


tax_invoice_product_with_subtract_post_schema = {
    "notes": "Create tax invoice product with purchase products_left subtraction.",
    "nickname": "Create tax invoice product. with purchase products_left subtraction.",
    "parameters": [
        {
            "name": "Create tax invoice product with "
            "purhcase products_left subtraction.",
            "description": "TaxInvoiceProduct 'tax_invoice_id', "
            "'sale_invoice_product_id', 'purchase_invoice_products_id'"
            " and 'quantity' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"tax_invoice_id": 1, "sale_invoice_product_id": 1, '
            '"purchase_invoice_product_id": 1, "quantity": 2}',
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
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


tax_invoice_product_with_adding_products_left_delete_schema = {
    "notes": "Delete tax invoice product data by id with"
    " adding purchase products_left.",
    "nickname": "Delete tax invoice product with adding purchase products_left.",
    "responseClass": '{"message": "Tax invoice product was successfully deleted."}',
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
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


tax_invoice_with_purchase_add_products_left_delete_schema = {
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
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
