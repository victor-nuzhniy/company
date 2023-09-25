"""Swagger schemas for user apps."""

user_schema = {
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
        }
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}
