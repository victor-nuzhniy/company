"""Schemas for order base apps."""
from api.common.constants import (
    authorization_parameter,
    code_conflict,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

order_get_schema = {
    "notes": "Get base by id.",
    "nickname": "Get base.",
    "responseClass": "OrderFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


order_put_schema = {
    "notes": "Update base data by id.",
    "nickname": "Update base.",
    "parameters": [
        {
            "name": "Update base",
            "description": "Order 'user_id', 'name' and 'customer_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"user_id": 1, "name": "O-000234", "customer_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderFields",
    "responseMessages": response_message_list,
}


order_patch_schema = {
    "notes": "Partially update base data by id.",
    "nickname": "Partially update base.",
    "parameters": [
        {
            "name": "Partially update base",
            "description": "".join(
                (
                    "Order 'user_id', 'name', 'created_at' and ",
                    "'customer_id' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"user_id": 1, "name": "O-000234", ',
                    '"created_at": "2023-10-01", "customer_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderFields",
    "responseMessages": response_message_list,
}


order_delete_schema = {
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


order_post_schema = {
    "notes": "Create base.",
    "nickname": "Create base.",
    "parameters": [
        {
            "name": "Create base",
            "description": "Order 'user_id', 'name' and 'customer_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"user_id": 1, "name": "O-000234", "customer_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderFields",
    "responseMessages": response_message_list,
}


orders_get_schema = {
    "notes": "Get all orders.",
    "nickname": "Get all orders.",
    "responseClass": "OrderFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


order_product_get_schema = {
    "notes": "Get base base by id.",
    "nickname": "Get base base.",
    "responseClass": "OrderProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


order_product_put_schema = {
    "notes": "Update base base data by id.",
    "nickname": "Update base base.",
    "parameters": [
        {
            "name": "Update base base",
            "description": "".join(
                (
                    "OrderProduct 'product_id', 'quantity', 'price' ",
                    "and 'order_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, "price": 100,',
                    ' "order_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderProductFields",
    "responseMessages": response_message_list,
}


order_product_patch_schema = {
    "notes": "Partially update base base data by id.",
    "nickname": "Partially update base base.",
    "parameters": [
        {
            "name": "Partially update base base",
            "description": "".join(
                (
                    "OrderProduct 'product_id', 'quantity', 'price' ",
                    "and 'order_id' fields.",
                ),
            ),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, "price": 100,',
                    ' "order_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderProductFields",
    "responseMessages": response_message_list,
}


order_product_delete_schema = {
    "notes": "Delete base base data by id.",
    "nickname": "Delete base base.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_conflict,
    ],
}


order_product_post_schema = {
    "notes": "Create base base.",
    "nickname": "Create base base.",
    "parameters": [
        {
            "name": "Create base base",
            "description": "".join(
                (
                    "OrderProduct 'product_id', 'quantity', 'price' ",
                    "and 'order_id' fields.",
                ),
            ),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"product_id": 1, "quantity": 2, "price": 100,',
                    ' "order_id": 1}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderProductFields",
    "responseMessages": response_message_list,
}


order_products_get_schema = {
    "notes": "Get all base products.",
    "nickname": "Get all base products.",
    "responseClass": "OrderProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
