"""Swagger schemas for auth apps."""
from api.constants import (
    code_access_denied,
    code_does_not_exist,
    code_server,
    code_success,
    code_unsupported_media_type,
)

login_schema = {
    "notes": "Login routes.",
    "nickname": "Handle login post request.",
    "parameters": [
        {
            "name": "Login data",
            "description": "User email and password",
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"email": "ab@abc.com", "password": "111"}',
        },
    ],
    "responseClass": "".join(
        (
            '{"message": "Successfully fetched auth token",',
            ' "data": "some_token"}',
        ),
    ),
    "responseMessages": [
        code_success,
        {
            "code": 404,
            "message": "Error fetching auth token!, invalid email or password",
        },
        code_does_not_exist,
        code_unsupported_media_type,
        code_server,
    ],
}

admin_schema = {
    "notes": "Admin routes.",
    "nickname": "Create active admin user.",
    "parameters": [
        {
            "name": "Admin data",
            "description": "User email and password, admin password",
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join(
                (
                    '{"username": "Vasja", "email": "ab@abc.com", ',
                    '"password": "111", "admin_password": "123"}',
                ),
            ),
        },
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        code_success,
        code_access_denied,
        code_unsupported_media_type,
        {
            "code": 422,
            "message": "".join(
                (
                    "Invalid input. Enter valid value. ",
                    "Too long value. Access field is empty.",
                ),
            ),
        },
    ],
}
