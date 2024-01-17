"""Schemas for order apps."""
from api.constants import (
    authorization_parameter,
    code_does_not_exist,
    code_unauthorized,
    response_message_list,
    small_response_message_list,
)

order_get_schema = {
    "notes": "Get order by id.",
    "nickname": "Get order.",
    "responseClass": "OrderFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


order_put_schema = {
    "notes": "Update order data by id.",
    "nickname": "Update order.",
    "parameters": [
        {
            "name": "Update order",
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
    "notes": "Partially update order data by id.",
    "nickname": "Partially update order.",
    "parameters": [
        {
            "name": "Partially update order",
            "description": "".join((
                "Order 'user_id', 'name', 'created_at' and ",
                "'customer_id' fields.",
            )),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"user_id": 1, "name": "O-000234", ',
                '"created_at": "2023-10-01", "customer_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderFields",
    "responseMessages": response_message_list,
}


order_delete_schema = {
    "notes": "Delete order data by id.",
    "nickname": "Delete order.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


order_post_schema = {
    "notes": "Create order.",
    "nickname": "Create order.",
    "parameters": [
        {
            "name": "Create order",
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
    "notes": "Get order product by id.",
    "nickname": "Get order product.",
    "responseClass": "OrderProductFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


order_product_put_schema = {
    "notes": "Update order product data by id.",
    "nickname": "Update order product.",
    "parameters": [
        {
            "name": "Update order product",
            "description": "".join((
                "OrderProduct 'product_id', 'quantity', 'price' ",
                "and 'order_id' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"product_id": 1, "quantity": 2, "price": 100,',
                ' "order_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderProductFields",
    "responseMessages": response_message_list,
}


order_product_patch_schema = {
    "notes": "Partially update order product data by id.",
    "nickname": "Partially update order product.",
    "parameters": [
        {
            "name": "Partially update order product",
            "description": "".join((
                "OrderProduct 'product_id', 'quantity', 'price' ",
                "and 'order_id' fields.",
            )),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"product_id": 1, "quantity": 2, "price": 100,',
                ' "order_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderProductFields",
    "responseMessages": response_message_list,
}


order_product_delete_schema = {
    "notes": "Delete order product data by id.",
    "nickname": "Delete order product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}


order_product_post_schema = {
    "notes": "Create order product.",
    "nickname": "Create order product.",
    "parameters": [
        {
            "name": "Create order product",
            "description": "".join((
                "OrderProduct 'product_id', 'quantity', 'price' ",
                "and 'order_id' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"product_id": 1, "quantity": 2, "price": 100,',
                ' "order_id": 1}',
            )),
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderProductFields",
    "responseMessages": response_message_list,
}


order_products_get_schema = {
    "notes": "Get all order products.",
    "nickname": "Get all order products.",
    "responseClass": "OrderProductFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
