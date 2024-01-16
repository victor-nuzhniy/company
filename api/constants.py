"""Contstants for api app."""


INVOICE_NAME_PREFIX = "I-0000"
TAX_INVOICE_NAME_PREFIX = "T-0000"
SALE_INVOICE_NAME_PREFIX = "S-0000"

code_success: dict = {"code": 200, "message": "Operation successfully performed"}
code_error: dict = {"code": 400, "message": "Error (specified)."}
code_unauthorized: dict = {"code": 401, "message": "Unauthorized."}
code_access_denied: dict = {"code": 403, "message": "Access denied. Value is invalid."}
code_not_found: dict = {"code": 404, "message": "Not found."}
code_does_not_exist: dict = {
    "code": 409, "message": "Instance with id does not exist.",
}
code_unsupported_media_type: dict = {"code": 415, "message": "Unsupported media type."}
code_invalid_input: dict = {"code": 422, "message": "Invalid input (specified)."}
code_server: dict = {"code": 500, "message": "Something went wrong"}

response_message_list: list[dict] = [
    code_success,
    code_error,
    code_unauthorized,
    code_does_not_exist,
    code_invalid_input,
]

authorization_parameter = [{
    "name": "Authorization",
    "description": "Authorization: Bearer token",
    "required": True,
    "allowMultiple": False,
    "dataType": "String",
    "paramType": "header",
    "defaultValue": "Bearer ",
}]
