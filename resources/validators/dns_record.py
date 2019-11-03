from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema


schema = {
    'type': 'object',
    'properties': {
        'recordName': {'type': 'string'},
        'recordType': {'type': 'string'},
        'ttl': {'type': 'integer'},
        'answer': {'type': 'string'}
    },
    'required': ['recordName', 'recordType', 'answer']
}


class DNSRecordJSONValidator(Inputs):
    json = [JsonSchema(schema=schema)]

