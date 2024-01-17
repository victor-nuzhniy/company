"""Swagger schemas for user apps."""
from api.constants import (
    authorization_parameter,
    response_message_list,
    small_response_message_list,
)

user_get_schema = {
    "notes": "Get user by id.",
    "nickname": "Get user.",
    "responseClass": "UserFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}


user_put_schema = {
    "notes": "Update user data by id.",
    "nickname": "Update user.",
    "parameters": [
        {
            "name": "Update user",
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
    "notes": "Partially update user data by id.",
    "nickname": "Partially update user.",
    "parameters": [
        {
            "name": "Partially update user",
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
    "notes": "Delete user data by id.",
    "nickname": "Delete user.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}


user_post_schema = {
    "notes": "Create user.",
    "nickname": "Create user.",
    "parameters": [
        {
            "name": "Create user",
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
