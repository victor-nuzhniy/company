"""Schemas for counterparty apps."""


discount_get_schema = {
    "notes": "Get discount by id.",
    "nickname": "Get discount.",
    "responseClass": "DiscountFields",
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


discount_put_schema = {
    "notes": "Update discount data by id.",
    "nickname": "Update discount.",
    "parameters": [
        {
            "name": "Update discount",
            "description": "Discount 'name' and 'rate' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "enterprise", "rate": 10}',
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
    "responseClass": "DiscountFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


discount_patch_schema = {
    "notes": "Partially update discount data by id.",
    "nickname": "Partially update discount.",
    "parameters": [
        {
            "name": "Partially update discount",
            "description": "Discount 'name' and 'rate' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "enterprise", "rate": 10}',
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
    "responseClass": "DiscountFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


discount_delete_schema = {
    "notes": "Delete discount data by id.",
    "nickname": "Delete discount.",
    "responseClass": '{"message": "Deleted instance with id"}',
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
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


discount_post_schema = {
    "notes": "Create discount.",
    "nickname": "Create discount.",
    "parameters": [
        {
            "name": "Create discount",
            "description": "Discount 'name' and 'rate' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "enterprise", "rate": 10}',
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
    "responseClass": "DiscountFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


discounts_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "DiscountFields",
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


counterparty_get_schema = {
    "notes": "Get counterparty by id.",
    "nickname": "Get counterparty.",
    "responseClass": "CounterpartyFields",
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}

counterparty_put_schema = {
    "notes": "Update counterparty data by id.",
    "nickname": "Update counterparty.",
    "parameters": [
        {
            "name": "Update counterparty",
            "description": "Counterparty 'name', 'postal_code', 'country',"
            " 'city', 'address', 'phone_number' and "
            "'discount_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "Alabama", "postal_code": "49000", '
            '"country": "Poland", "city": "Krakow, '
            '"address": "Nova str, 23/3/8", "phone_number":'
            ' "357 335", "dicount_id": 1}',
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
    "responseClass": "CounterpartyFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}

counterparty_patch_schema = {
    "notes": "Partially update counterparty data by id.",
    "nickname": "Partially update counterparty.",
    "parameters": [
        {
            "name": "Partially update counterparty",
            "description": "Counterparty 'name', 'postal_code', 'country',"
            " 'city', 'address', 'phone_number' and "
            "'discount_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "Alabama", "postal_code": "49000", '
            '"country": "Poland", "city": "Krakow, '
            '"address": "Nova str, 23/3/8", "phone_number":'
            ' "357 335", "dicount_id": 1}',
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
    "responseClass": "CounterpartyFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}

counterparty_delete_schema = {
    "notes": "Delete counterparty data by id.",
    "nickname": "Delete counterparty.",
    "responseClass": '{"message": "Deleted instance with id"}',
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
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}

counterparty_post_schema = {
    "notes": "Create counterparty.",
    "nickname": "Create counterparty.",
    "parameters": [
        {
            "name": "Create counterparty",
            "description": "Counterparty 'name', 'postal_code', 'country',"
            " 'city', 'address', 'phone_number' and "
            "'discount_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "Alabama", "postal_code": "49000", '
            '"country": "Poland", "city": "Krakow, '
            '"address": "Nova str, 23/3/8", "phone_number":'
            ' "357 335", "dicount_id": 1}',
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
    "responseClass": "CounterpartyFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}

counterparties_get_schema = {
    "notes": "Get all counterparties.",
    "nickname": "Get all counterparties.",
    "responseClass": "CounterpartyFields",
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


agreement_get_schema = {
    "notes": "Get agreement by id.",
    "nickname": "Get agreement.",
    "responseClass": "AgreementFields",
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


agreement_put_schema = {
    "notes": "Update agreement data by id.",
    "nickname": "Update agreement.",
    "parameters": [
        {
            "name": "Update agreement",
            "description": "Agreement 'name' and 'counterparty_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "Agreement 1", "counterparty_id": 1}',
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
    "responseClass": "AgreementFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


agreement_patch_schema = {
    "notes": "Partially update agreement data by id.",
    "nickname": "Partially update agreement.",
    "parameters": [
        {
            "name": "Partially update agreement",
            "description": "Agreement 'name' and 'counterparty_id' fields.",
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "Agreement 1", "counterparty_id": 1}',
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
    "responseClass": "AgreementFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


agreement_delete_schema = {
    "notes": "Delete agreement data by id.",
    "nickname": "Delete agreement.",
    "responseClass": '{"message": "Deleted instance with id"}',
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
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}


agreement_post_schema = {
    "notes": "Create agreement.",
    "nickname": "Create agreement.",
    "parameters": [
        {
            "name": "Create agreement",
            "description": "Agreement 'name' and 'counterparty_id' fields.",
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": '{"name": "Agreement 1", "counterparty_id": 1}',
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
    "responseClass": "AgreementFields",
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
        {"code": 415, "message": "Invalid input."},
    ],
}


agreements_get_schema = {
    "notes": "Get all agreements.",
    "nickname": "Get all agreements.",
    "responseClass": "AgreementFields",
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
    "responseMessages": [
        {"code": 200, "message": "Operation successfully performed"},
        {"code": 409, "message": "Instance with id does not exist."},
    ],
}
