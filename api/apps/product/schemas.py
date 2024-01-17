"""Schemas for product apps."""
from api.constants import (
    authorization_parameter,
    code_does_not_exist,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

product_get_schema = {
    "notes": "Get product by id.",
    "nickname": "Get product.",
    "responseClass": "ProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


product_put_schema = {
    "notes": "Update product data by id.",
    "nickname": "Update product.",
    "parameters": [
        {
            "name": "Update product",
            "description": "".join((
                "Product 'name', 'code', 'units', 'currency', ",
                "'price' and 'product_type_id' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "sugar", "code": "123456", "units": "kg",',
                ' "currency": "uah", "price": 100, "product_type_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductFields",
    "responseMessages": response_message_list,
}


product_patch_schema = {
    "notes": "Partially update product data by id.",
    "nickname": "Partially update product.",
    "parameters": [
        {
            "name": "Partially update product",
            "description": "".join((
                "Product 'name', 'code', 'units', 'currency', ",
                "'price' and 'product_type_id' fields.",
            )),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "sugar", "code": "123456", "units": "kg",',
                ' "currency": "uah", "price": 100, "product_type_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductFields",
    "responseMessages": response_message_list,
}


product_delete_schema = {
    "notes": "Delete product data by id.",
    "nickname": "Delete product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


product_post_schema = {
    "notes": "Create product.",
    "nickname": "Create product.",
    "parameters": [
        {
            "name": "Create product",
            "description": "".join((
                "Product 'name', 'code', 'units', 'currency', ",
                "'price' and 'product_type_id' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "sugar", "code": "123456", "units": "kg",',
                ' "currency": "uah", "price": 100, "product_type_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductFields",
    "responseMessages": response_message_list,
}


products_get_schema = {
    "notes": "Get all products.",
    "nickname": "Get all products.",
    "responseClass": "ProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


product_type_get_schema = {
    "notes": "Get product type by id.",
    "nickname": "Get product type.",
    "responseClass": "ProductTypeFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
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
    ]
    + authorization_parameter,
    "responseClass": "ProductTypeFields",
    "responseMessages": response_message_list,
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
    ]
    + authorization_parameter,
    "responseClass": "ProductTypeFields",
    "responseMessages": response_message_list,
}


product_type_delete_schema = {
    "notes": "Delete product type data by id.",
    "nickname": "Delete product type.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
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
    ]
    + authorization_parameter,
    "responseClass": "ProductTypeFields",
    "responseMessages": response_message_list,
}


product_types_get_schema = {
    "notes": "Get all product types.",
    "nickname": "Get all product types.",
    "responseClass": "ProductTypeFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
