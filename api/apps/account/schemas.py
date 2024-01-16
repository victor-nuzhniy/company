"""Swagger schemas for account apps."""
from api.constants import (
    authorization_parameter,
    code_success,
    code_unauthorized,
    code_unsupported_media_type,
    response_message_list,
)

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
    ]
    + authorization_parameter,
    "responseClass": "{'message': 'info'}",
    "responseMessages": response_message_list,
}


period_report_schema = {
    "notes": "Create period report",
    "responseClass": "PeriodReport",
    "nickname": "Create period report",
    "parameters": [
        {
            "name": "Date period",
            "description": "Start and end period dates, format '%y-%m-%d'",  # noqa WPS323
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date_from": "2020-01-01", "date_to": "2024-01-01"}',
        },
    ]
    + authorization_parameter,
    "responseMessages": response_message_list,
}


product_leftovers_schema = {
    "notes": "Product leftovers to particular date.",
    "responseClass": "ProductLeftovers",
    "nickname": "Calculate income for given period",
    "parameters": [
        {
            "name": "Date",
            "description": "Date to evaluate product leftovers, format '%y-%m-%d'",  # noqa WPS323
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date": "2024-01-01"}',
        },
    ]
    + authorization_parameter,
    "responseMessages": [
        code_success,
        code_unauthorized,
        code_unsupported_media_type,
    ],
}


income_for_period_schema = {
    "notes": "Calculate income for given period.",
    "responseClass": "IncomeForPeriod",
    "nickname": "Create period report",
    "parameters": [
        {
            "name": "Date period",
            "description": "Start and end period dates, format '%y-%m-%d'",  # noqa WPS323
            "required": True,
            "allowMultiple": False,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"date_from": "2020-01-01", "date_to": "2024-01-01"}',
        },
    ]
    + authorization_parameter,
    "responseMessages": [
        code_success,
        code_unauthorized,
        code_unsupported_media_type,
    ],
}
