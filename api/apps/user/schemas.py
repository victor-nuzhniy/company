"""Swagger schemas for user apps."""

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
        }
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


user_get_schema = {
    "notes": "Get user by id.",
    "nickname": "Get user.",
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
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
            "defaultValue": '{"username": "Alex", "email": "a@a.com"}',
        }
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
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
            "defaultValue": '{"username": "Alex", "email": "a@a.com"}',
        }
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


user_delete_schema = {
    "notes": "Delete user data by id.",
    "nickname": "Delete user.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
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
            "defaultValue": '{"username": "Alex", "email": "a@a.com",'
            ' "password": "111"}',
        }
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


users_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
