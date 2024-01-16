"""Schemas for common_services apps."""


name_number_schema = {
    "notes": "Get number for document name based on last name number.",
    "nickname": "Get number for document name based on last name number.",
    "parameters": [
        {
            "name": "Authorization",
            "description": "Authorization: Bearer token",
            "required": True,
            "allowMultiple": False,
            "dataType": "String",
            "paramType": "header",
            "defaultValue": "Bearer ",
        },
    ],
    "responseClass": "NameNumber",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {
            "code": 409,
            "message": "".join((
                "'model_name' is not in Order, Invoice,",
                " PurchaseInvoice, SaleInvoice, TaxInvoice models.",
            )),
        },
    ],
}
