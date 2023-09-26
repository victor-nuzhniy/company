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
        }
    ],
    "responseClass": "{'message': 'info'}",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


period_report_schema = {
    "notes": "Create period report",
    "responseClass": "PeriodReport",
    "nickname": "Create period report",
    "parameters": [
        {
            "name": "Date period",
            "description": "Start and end period dates, format '%y-%m-%d'",
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date_from": "2020-01-01", "date_to": "2024-01-01"}',
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Product not enough to process invoice with id."},
        {"code": 415, "message": "Invalid input."},
    ],
}


product_leftovers_schema = {
    "notes": "Product leftovers to particular date.",
    "responseClass": "ProductLeftovers",
    "nickname": "Calculate income for given period",
    "parameters": [
        {
            "name": "Date",
            "description": "Date to evaluate product leftovers, format '%y-%m-%d'",
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date": "2024-01-01"}',
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
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
            "description": "Start and end period dates, format '%y-%m-%d'",
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date_from": "2020-01-01", "date_to": "2024-01-01"}',
        },
    ],
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 415, "message": "Invalid input."},
    ],
}