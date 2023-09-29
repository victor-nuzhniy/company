"""Schemas for product apps."""


product_get_schema = {
    "notes": "Get product by id.",
    "nickname": "Get product.",
    "responseClass": "ProductFields",
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
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
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
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


product_delete_schema = {
    "notes": "Delete product data by id.",
    "nickname": "Delete product.",
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
    "responseClass": "ProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


products_get_schema = {
    "notes": "Get all products.",
    "nickname": "Get all products.",
    "responseClass": "ProductFields",
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


product_type_get_schema = {
    "notes": "Get product type by id.",
    "nickname": "Get product type.",
    "responseClass": "ProductTypeFields",
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
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
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
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


product_type_delete_schema = {
    "notes": "Delete product type data by id.",
    "nickname": "Delete product type.",
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
    "responseClass": "ProductTypeFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


product_types_get_schema = {
    "notes": "Get all product types.",
    "nickname": "Get all product types.",
    "responseClass": "ProductTypeFields",
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
