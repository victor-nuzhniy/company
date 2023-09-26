"""Schemas for product apps."""


product_get_schema = {
    "notes": "Get product by id.",
    "nickname": "Get product.",
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_put_schema = {
    "notes": "Update product data by id.",
    "nickname": "Update product.",
    "parameters": [
        {
            "name": "Update product",
            "description": "Product 'name', 'code', 'units', 'currency', "
            "'price' and 'product_type_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "sugar", "code": "123456", "units": "kg",'
            ' "currency": "uah", "price": 100, "product_type_id": 1}',
        }
    ],
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_patch_schema = {
    "notes": "Partially update product data by id.",
    "nickname": "Partially update product.",
    "parameters": [
        {
            "name": "Partially update product",
            "description": "Product 'name', 'code', 'units', 'currency', "
            "'price' and 'product_type_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "sugar", "code": "123456", "units": "kg",'
            ' "currency": "uah", "price": 100, "product_type_id": 1}',
        }
    ],
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_delete_schema = {
    "notes": "Delete product data by id.",
    "nickname": "Delete product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


product_post_schema = {
    "notes": "Create product.",
    "nickname": "Create product.",
    "parameters": [
        {
            "name": "Create product",
            "description": "Product 'name', 'code', 'units', 'currency', "
            "'price' and 'product_type_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "sugar", "code": "123456", "units": "kg",'
            ' "currency": "uah", "price": 100, "product_type_id": 1}',
        }
    ],
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


products_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


product_type_get_schema = {
    "notes": "Get product type by id.",
    "nickname": "Get product type.",
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_type_put_schema = {
    "notes": "Update product type data by id.",
    "nickname": "Update product type.",
    "parameters": [
        {
            "name": "Update product type",
            "description": "ProductType 'name' field.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "product"}',
        }
    ],
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_type_patch_schema = {
    "notes": "Partially update product type data by id.",
    "nickname": "Partially update product type.",
    "parameters": [
        {
            "name": "Partially update product type",
            "description": "ProductType 'name' field.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "product"}',
        }
    ],
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_type_delete_schema = {
    "notes": "Delete product type data by id.",
    "nickname": "Delete product type.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


product_type_post_schema = {
    "notes": "Create product type.",
    "nickname": "Create product type.",
    "parameters": [
        {
            "name": "Create product type",
            "description": "ProductType 'name' field.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "product"}',
        }
    ],
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_types_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
