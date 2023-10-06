"""Schemas for purchase apps."""


purchase_invoice_get_schema = {
    "notes": "Get purchase invoice by id.",
    "nickname": "Get purchase invoice.",
    "responseClass": "PurchaseInvoiceFields",
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
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
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
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoice_patch_schema = {
    "notes": "Partially update purchase invoice data by id.",
    "nickname": "Partially update purchase invoice.",
    "parameters": [
        {
            "name": "Partially update purchase invoice",
            "description": "PurchaseInvoice 'name', 'agreement_id' and "
            "'created_at fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "P-000012345", "agreement_id": 1, '
            '"created_at": "2023-09-20"}',
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
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoice_delete_schema = {
    "notes": "Delete purchase invoice data by id.",
    "nickname": "Delete purchase invoice.",
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
    "responseClass": "PurchaseInvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoices_get_schema = {
    "notes": "Get all purchase invoices.",
    "nickname": "Get all purchase invoices.",
    "responseClass": "PurchaseInvoiceFields",
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


purchase_invoice_product_get_schema = {
    "notes": "Get purchase invoice product by id.",
    "nickname": "Get purchase invoice product.",
    "responseClass": "PurchaseInvoiceProductFields",
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
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoice_product_put_schema = {
    "notes": "Update purchase invoice product data by id.",
    "nickname": "Update purchase invoice product.",
    "parameters": [
        {
            "name": "Update purchase invoice product",
            "description": "PurchaseInvoiceProduct 'product_id', 'quantity', "
            "'price', 'purchase_invoice_id' and 'products_left' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, "price": 100, '
            '"purchase_invoice_id": 1, "products_left": 100}',
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
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoice_product_patch_schema = {
    "notes": "Partially update purchase invoice product data by id.",
    "nickname": "Partially update purchase invoice product.",
    "parameters": [
        {
            "name": "Partially update purchase invoice product",
            "description": "PurchaseInvoiceProduct 'product_id', 'quantity', "
            "'price', 'purchase_invoice_id' and 'product_left' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, "price": 100, '
            '"purchase_invoice_id": 1, "products_left": 100}',
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
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoice_product_delete_schema = {
    "notes": "Delete purchase invoice product data by id.",
    "nickname": "Delete purchase invoice product.",
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


purchase_invoice_product_post_schema = {
    "notes": "Create purchase invoice product.",
    "nickname": "Create purchase invoice product.",
    "parameters": [
        {
            "name": "Create purchase invoice product",
            "description": "PurchaseInvoiceProduct 'product_id', 'quantity', "
            "'price', 'purchase_invoice_id' and 'product_left' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, "price": 100, '
            '"purchase_invoice_id": 1, "products_left": 100}',
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
    "responseClass": "PurchaseInvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


purchase_invoice_products_get_schema = {
    "notes": "Get all purchase invoice products.",
    "nickname": "Get all purchase invoice products.",
    "responseClass": "PurchaseInvoiceProductFields",
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


purchase_registry_get_schema = {
    "notes": "Get purchase registry.",
    "nickname": "Get purchase registry.",
    "responseClass": "PurchaseRegistryFields",
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
            "defaultValue": 10,
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
    ],
}


purchase_invoices_products_get_schema = {
    "notes": "Get purchase invoice products by purchase invoice id.",
    "nickname": "Get purchase invoice products by purchase invoice id.",
    "responseClass": "PurchaseInvoiceProductFields",
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
