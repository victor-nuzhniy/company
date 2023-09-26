"""Schemas for invoice apps."""

invoice_get_schema = {
    "notes": "Get invoice by id.",
    "nickname": "Get invoice.",
    "responseClass": "InvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_put_schema = {
    "notes": "Update invoice data by id.",
    "nickname": "Update invoice.",
    "parameters": [
        {
            "name": "Update invoice",
            "description": "Invoice 'name', 'order_id' and 'agreement_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "I-00357", "order_id": 1, "agreement_id": 1}',
        }
    ],
    "responseClass": "InvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_patch_schema = {
    "notes": "Partially update invoice data by id.",
    "nickname": "Partially update invoice.",
    "parameters": [
        {
            "name": "Partially update invoice",
            "description": "Invoice 'name', 'order_id', 'created_at' "
            "and 'agreement_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "I-00357", "order_id": 1, '
            '"created_at": "2023-10-01", "agreement_id": 1}',
        }
    ],
    "responseClass": "InvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_delete_schema = {
    "notes": "Delete invoice data by id.",
    "nickname": "Delete invoice.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


invoice_post_schema = {
    "notes": "Create invoice.",
    "nickname": "Create invoice.",
    "parameters": [
        {
            "name": "Create invoice",
            "description": "Invoice 'name', 'order_id' and 'agreement_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "I-00357", "order_id": 1, "agreement_id": 1}',
        }
    ],
    "responseClass": "InvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoices_get_schema = {
    "notes": "Get all invoices.",
    "nickname": "Get all invoices.",
    "responseClass": "InvoiceFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


invoice_product_get_schema = {
    "notes": "Get invoice product by id.",
    "nickname": "Get invoice product.",
    "responseClass": "InvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_product_put_schema = {
    "notes": "Update invoice product data by id.",
    "nickname": "Update invoice product.",
    "parameters": [
        {
            "name": "Update invoice product",
            "description": "Invoice product 'product_id', "
            "'quantity', 'price' and 'invoice_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, '
            '"price": 100, "invoice_id": 1}',
        }
    ],
    "responseClass": "InvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_product_patch_schema = {
    "notes": "Partially update invoice product data by id.",
    "nickname": "Partially update invoice product.",
    "parameters": [
        {
            "name": "Partially update invoice product",
            "description": "Invoice product 'product_id', "
            "'quantity', 'price' and 'invoice_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, '
            '"price": 100, "invoice_id": 1}',
        }
    ],
    "responseClass": "InvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_product_delete_schema = {
    "notes": "Delete invoice product data by id.",
    "nickname": "Delete invoice product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


invoice_product_post_schema = {
    "notes": "Create invoice product.",
    "nickname": "Create invoice product.",
    "parameters": [
        {
            "name": "Create invoice product",
            "description": "Invoice product 'product_id', "
            "'quantity', 'price' and 'invoice_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, '
            '"price": 100, "invoice_id": 1}',
        }
    ],
    "responseClass": "InvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


invoice_products_get_schema = {
    "notes": "Get all invoice products.",
    "nickname": "Get all invoice products.",
    "responseClass": "InvoiceProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
