"""Schemas for counterparty special apps."""
from api.common.constants import authorization_parameter, small_response_message_list

counterparty_agreements_get_schema = {
    "notes": "Get agreements by base id.",
    "nickname": "Get agreements by base id.",
    "responseClass": "AgreementFields",
    "parameters": authorization_parameter,
    "responseMessages": small_response_message_list,
}
