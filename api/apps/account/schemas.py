"""Swagger schemas for account apps."""


process_sale_invoice_schema = {
    "notes": "Operations with saling process",
    "nickname": "Process sale invoice",
    "parameters": [
        {
            "name": "sale_invoice_id",
            "description": "Sale invoice id",
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"sale_invoice_id": 1}',
        },
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
    "responseClass": "{'message': 'info'}",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


period_report_schema = {
    "notes": "Create period report",
    "responseClass": "PeriodReport",
    "nickname": "Create period report",
    "parameters": [
        {
            "name": "Date period",
            "description": "Start and end period dates, format '%y-%m-%d'",   # noqa WPS323
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date_from": "2020-01-01", "date_to": "2024-01-01"}',
        },
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 400, "message": "Invalid input (specified)."},
        {"code": 401, "message": "Unauthorized."},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 422, "message": "Invalid input (specified)."},
    ],
}


product_leftovers_schema = {
    "notes": "Product leftovers to particular date.",
    "responseClass": "ProductLeftovers",
    "nickname": "Calculate income for given period",
    "parameters": [
        {
            "name": "Date",
            "description": "Date to evaluate product leftovers, format '%y-%m-%d'",   # noqa WPS323
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date": "2024-01-01"}',
        },
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 401, "message": "Unauthorized."},
        {"code": 415, "message": "Invalid input."},
    ],
}


income_for_period_schema = {
    "notes": "Calculate income for given period.",
    "responseClass": "IncomeForPeriod",
    "nickname": "Create period report",
    "parameters": [
        {
            "name": "Date period",
            "description": "Start and end period dates, format '%y-%m-%d'",   # noqa WPS323
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date_from": "2020-01-01", "date_to": "2024-01-01"}',
        },
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 401, "message": "Unauthorized."},
        {"code": 415, "message": "Invalid input."},
    ],
}
