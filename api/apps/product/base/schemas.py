"""Schemas for product base apps."""
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

product_get_schema = {
    "notes": "Get base by id.",
    "nickname": "Get base.",
    "responseClass": "ProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


product_put_schema = {
    "notes": "Update base data by id.",
    "nickname": "Update base.",
    "parameters": [
        {
            "name": "Update base",
            "description": "".join(
                (
                    "Product 'name', 'code', 'units', 'currency', ",
                    "'price' and 'product_type_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "sugar", "code": "123456", "units": "kg",',
                    ' "currency": "uah", "price": 100, "product_type_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductFields",
    "responseMessages": response_message_list,
}


product_patch_schema = {
    "notes": "Partially update base data by id.",
    "nickname": "Partially update base.",
    "parameters": [
        {
            "name": "Partially update base",
            "description": "".join(
                (
                    "Product 'name', 'code', 'units', 'currency', ",
                    "'price' and 'product_type_id' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "sugar", "code": "123456", "units": "kg",',
                    ' "currency": "uah", "price": 100, "product_type_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductFields",
    "responseMessages": response_message_list,
}


product_delete_schema = {
    "notes": "Delete base data by id.",
    "nickname": "Delete base.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


product_post_schema = {
    "notes": "Create base.",
    "nickname": "Create base.",
    "parameters": [
        {
            "name": "Create base",
            "description": "".join(
                (
                    "Product 'name', 'code', 'units', 'currency', ",
                    "'price' and 'product_type_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"name": "sugar", "code": "123456", "units": "kg",',
                    ' "currency": "uah", "price": 100, "product_type_id": 1}',
                ),
            ),
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
    "notes": "Get base type by id.",
    "nickname": "Get base type.",
    "responseClass": "ProductTypeFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


product_type_put_schema = {
    "notes": "Update base type data by id.",
    "nickname": "Update base type.",
    "parameters": [
        {
            "name": "Update base type",
            "description": "ProductType 'name' field.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "base"}',
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductTypeFields",
    "responseMessages": response_message_list,
}


product_type_patch_schema = {
    "notes": "Partially update base type data by id.",
    "nickname": "Partially update base type.",
    "parameters": [
        {
            "name": "Partially update base type",
            "description": "ProductType 'name' field.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "base"}',
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductTypeFields",
    "responseMessages": response_message_list,
}


product_type_delete_schema = {
    "notes": "Delete base type data by id.",
    "nickname": "Delete base type.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


product_type_post_schema = {
    "notes": "Create base type.",
    "nickname": "Create base type.",
    "parameters": [
        {
            "name": "Create base type",
            "description": "ProductType 'name' field.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "base"}',
        },
    ]
    + authorization_parameter,
    "responseClass": "ProductTypeFields",
    "responseMessages": response_message_list,
}


product_types_get_schema = {
    "notes": "Get all base types.",
    "nickname": "Get all base types.",
    "responseClass": "ProductTypeFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
