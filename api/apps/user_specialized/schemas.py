"""Schemas for user_specialized apps."""
from api.constants import (
    authorization_parameter,
    code_access_denied,
    response_message_list,
)

user_admin_schema = {
    "notes": "Admin user operations.",
    "nickname": "Modify user 'is_active' or/and 'is_admin' fields.",
    "parameters": [
        {
            "name": "User status",
            "description": "User 'is_active' or/and 'is_admin' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"is_active": 1, "is_amdin": 1}',
        },
    ]
    + authorization_parameter,
    "responseClass": "UserFields",
    "responseMessages": response_message_list + [code_access_denied],
}
