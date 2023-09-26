"""Schemas for order apps."""

order_get_schema = {
    "notes": "Get order by id.",
    "nickname": "Get order.",
    "responseClass": "OrderFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
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
        }
    ],
    "responseClass": "OrderFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


order_patch_schema = {
    "notes": "Partially update order data by id.",
    "nickname": "Partially update order.",
    "parameters": [
        {
            "name": "Partially update order",
            "description": "Order 'user_id', 'name' and 'customer_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"user_id": 1, "name": "O-000234", "customer_id": 1}',
        }
    ],
    "responseClass": "OrderFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


order_delete_schema = {
    "notes": "Delete order data by id.",
    "nickname": "Delete order.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
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
        }
    ],
    "responseClass": "OrderFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


orders_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "OrderFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


order_product_get_schema = {
    "notes": "Get order product by id.",
    "nickname": "Get order product.",
    "responseClass": "OrderProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


order_product_put_schema = {
    "notes": "Update order product data by id.",
    "nickname": "Update order product.",
    "parameters": [
        {
            "name": "Update order product",
            "description": "OrderProduct 'product_id', 'quantity', 'price' "
            "and 'order_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, "price": 100,'
            ' "order_id": 1}',
        }
    ],
    "responseClass": "OrderProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


order_product_patch_schema = {
    "notes": "Partially update order product data by id.",
    "nickname": "Partially update order product.",
    "parameters": [
        {
            "name": "Partially update order product",
            "description": "OrderProduct 'product_id', 'quantity', 'price' "
            "and 'order_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, "price": 100,'
            ' "order_id": 1}',
        }
    ],
    "responseClass": "OrderProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


order_product_delete_schema = {
    "notes": "Delete order product data by id.",
    "nickname": "Delete order product.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


order_product_post_schema = {
    "notes": "Create order product.",
    "nickname": "Create order product.",
    "parameters": [
        {
            "name": "Create order product",
            "description": "OrderProduct 'product_id', 'quantity', 'price' "
            "and 'order_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"product_id": 1, "quantity": 2, "price": 100,'
            ' "order_id": 1}',
        }
    ],
    "responseClass": "OrderProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


order_products_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "OrderProductFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
