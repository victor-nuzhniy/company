"""Swagger schemas for user base apps."""
from api.common.constants import (
    authorization_parameter,
    response_message_list,
    small_response_message_list,
)

user_get_schema = {
    "notes": "Get base by id.",
    "nickname": "Get base.",
    "responseClass": "UserFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


user_put_schema = {
    "notes": "Update base data by id.",
    "nickname": "Update base.",
    "parameters": [
        {
            "name": "Update base",
            "description": "User 'username' and 'email' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"username": "Alex", "email": "a@a.com", ',
                    '"password": "111", "is_admin": 0, "is_active": 0}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "UserFields",
    "responseMessages": response_message_list,
}


user_patch_schema = {
    "notes": "Partially update base data by id.",
    "nickname": "Partially update base.",
    "parameters": [
        {
            "name": "Partially update base",
            "description": "User 'username' and 'email' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"username": "Alex", "email": "a@a.com", ',
                    '"password": "111", "is_admin": 0, "is_active": 0}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "UserFields",
    "responseMessages": response_message_list,
}


user_delete_schema = {
    "notes": "Delete base data by id.",
    "nickname": "Delete base.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


user_post_schema = {
    "notes": "Create base.",
    "nickname": "Create base.",
    "parameters": [
        {
            "name": "Create base",
            "description": "User 'username', 'email' and 'password' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"username": "Alex", "email": "a@a.com", ',
                    '"password": "111", "is_admin": 0, "is_active": 0}',
                ),
            ),
        },
    ]
    + authorization_parameter,
    "responseClass": "UserFields",
    "responseMessages": response_message_list,
}


users_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "UserFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
