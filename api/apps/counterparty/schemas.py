"""Schemas for counterparty apps."""
from api.constants import authorization_parameter, response_message_list, code_unauthorized, code_does_not_exist, \
    code_success

discount_get_schema = {
    "notes": "Get discount by id.",
    "nickname": "Get discount.",
    "responseClass": "DiscountFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
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
    ] + authorization_parameter,
    "responseClass": "DiscountFields",
    "responseMessages": response_message_list,
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
    ] + authorization_parameter,
    "responseClass": "DiscountFields",
    "responseMessages": response_message_list,
}

discount_delete_schema = {
    "notes": "Delete discount data by id.",
    "nickname": "Delete discount.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
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
    ] + authorization_parameter,
    "responseClass": "DiscountFields",
    "responseMessages": response_message_list,
}

discounts_get_schema = {
    "notes": "Get all users.",
    "nickname": "Get all users.",
    "responseClass": "DiscountFields",
    "parameters": authorization_parameter,
    "responseMessages": [
        code_success,
        code_unauthorized,
        code_does_not_exist,
    ],
}

counterparty_get_schema = {
    "notes": "Get counterparty by id.",
    "nickname": "Get counterparty.",
    "responseClass": "CounterpartyFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
}

counterparty_put_schema = {
    "notes": "Update counterparty data by id.",
    "nickname": "Update counterparty.",
    "parameters": [
        {
            "name": "Update counterparty",
            "description": "".join((
                "Counterparty 'name', 'postal_code', 'country',",
                " 'city', 'address', 'phone_number' and ",
                "'discount_id' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "Alabama", "postal_code": "49000", ',
                '"country": "Poland", "city": "Krakow, ',
                '"address": "Nova str, 23/3/8", "phone_number":',
                ' "357 335", "dicount_id": 1}',
            )),
        },
    ] + authorization_parameter,
    "responseClass": "CounterpartyFields",
    "responseMessages": response_message_list,
}

counterparty_patch_schema = {
    "notes": "Partially update counterparty data by id.",
    "nickname": "Partially update counterparty.",
    "parameters": [
        {
            "name": "Partially update counterparty",
            "description": "".join((
                "Counterparty 'name', 'postal_code', 'country',",
                " 'city', 'address', 'phone_number' and ",
                "'discount_id' fields.",
            )),
            "required": False,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "Alabama", "postal_code": "49000", ',
                '"country": "Poland", "city": "Krakow, ',
                '"address": "Nova str, 23/3/8", "phone_number":',
                ' "357 335", "dicount_id": 1}',
            )),
        },
    ] + authorization_parameter,
    "responseClass": "CounterpartyFields",
    "responseMessages": response_message_list,
}

counterparty_delete_schema = {
    "notes": "Delete counterparty data by id.",
    "nickname": "Delete counterparty.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
    ],
}

counterparty_post_schema = {
    "notes": "Create counterparty.",
    "nickname": "Create counterparty.",
    "parameters": [
        {
            "name": "Create counterparty",
            "description": "".join((
                "Counterparty 'name', 'postal_code', 'country',",
                " 'city', 'address', 'phone_number' and ",
                "'discount_id' fields.",
            )),
            "required": True,
            "allowMultiple": True,
            "dataType": "json",
            "paramType": "body",
            "defaultValue": "".join((
                '{"name": "Alabama", "postal_code": "49000", ',
                '"country": "Poland", "city": "Krakow, ',
                '"address": "Nova str, 23/3/8", "phone_number":',
                ' "357 335", "dicount_id": 1}',
            )),
        },
    ] + authorization_parameter,
    "responseClass": "CounterpartyFields",
    "responseMessages": response_message_list,
}

counterparties_get_schema = {
    "notes": "Get all counterparties.",
    "nickname": "Get all counterparties.",
    "responseClass": "CounterpartyFields",
    "parameters": authorization_parameter,
    "responseMessages": [
        code_success,
        code_unauthorized,
        code_does_not_exist,
    ],
}

agreement_get_schema = {
    "notes": "Get agreement by id.",
    "nickname": "Get agreement.",
    "responseClass": "AgreementFields",
    "parameters": authorization_parameter,
    "responseMessages": response_message_list,
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
    ] + authorization_parameter,
    "responseClass": "AgreementFields",
    "responseMessages": response_message_list,
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
    ] + authorization_parameter,
    "responseClass": "AgreementFields",
    "responseMessages": response_message_list,
}

agreement_delete_schema = {
    "notes": "Delete agreement data by id.",
    "nickname": "Delete agreement.",
    "responseClass": '{"message": "Deleted instance with id"}',
    "parameters": authorization_parameter,
    "responseMessages": [
        {"code": 200, "message": "Deleted instance with id."},
        code_unauthorized,
        code_does_not_exist,
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
    ] + authorization_parameter,
    "responseClass": "AgreementFields",
    "responseMessages": response_message_list,
}

agreements_get_schema = {
    "notes": "Get all agreements.",
    "nickname": "Get all agreements.",
    "responseClass": "AgreementFields",
    "parameters": authorization_parameter,
    "responseMessages": [
        code_success,
        code_unauthorized,
        code_does_not_exist,
    ],
}

counterparty_agreements_get_schema = {
    "notes": "Get agreements by counterparty id.",
    "nickname": "Get agreements by counterparty id.",
    "responseClass": "AgreementFields",
    "parameters": authorization_parameter,
    "responseMessages": [
        code_success,
        code_unauthorized,
        code_does_not_exist,
    ],
}
