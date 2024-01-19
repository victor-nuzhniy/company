"""Schemas for order special apps."""
from api.common.constants import (
    authorization_parameter,
    code_error,
    code_success,
    response_message_list,
    small_response_message_list,
)

order_registry_get_schema = {
    "notes": "Get base registry.",
    "nickname": "Get base registry.",
    "responseClass": "OrderRegistryFields",
    "parameters": authorization_parameter
    + [
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
            "description": "Query parameters date_from",
            "required": False,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "query",
            "defaultValue": "2020-01-01",
        },
        {
            "name": "date_to",
            "description": "Query parameters date_to",
            "required": False,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "query",
            "defaultValue": "2024-01-01",
        },
    ],
    "responseMessages": [
        code_success,
        code_error,
    ],
}


orders_products_get_schema = {
    "notes": "Get base products with additional info by base base id.",
    "nickname": "Get base products with additional info by base base id.",
    "responseClass": "OrdersProductsFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


user_order_post_schema = {
    "notes": "Create base with authenticated base.",
    "nickname": "Create base with authenticated base.",
    "parameters": [
        {
            "name": "Create base",
            "description": "Order 'name' and 'customer_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "O-000234", "customer_id": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "OrderFields",
    "responseMessages": response_message_list,
}


counterparty_orders_get_schema = {
    "notes": "Get orders by base id.",
    "nickname": "Get orders by base id.",
    "responseClass": "OrderFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
