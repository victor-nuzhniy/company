"""Swagger schemas for auth apps."""

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
        }
    ],
    "responseClass": '{"message": "Successfully fetched auth token",'
    ' "data": "some_token"}',
    "responseMessages": [
        {"code": 200, "message": "Successfully fetched auth token"},
        {
            "code": 404,
            "message": "Error fetching auth token!, invalid email or password",
        },
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
        {"code": 500, "message": "Something went wrong"},
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
            "defaultValue": '{"email": "ab@abc.com", "password": "111",'
            ' "admin_password": "123"}',
        }
    ],
    "responseClass": "UserFields",
    "responseMessages": [
        {"code": 200, "message": "Successfully fetched auth token"},
        {"code": 403, "message": "Access denied. Value is invalid."},
        {"code": 415, "message": "Invalid input."},
        {
            "code": 422,
            "message": "Invalid input. Enter valid value. "
            "Too long value. Access field is empty.",
        },
    ],
}
