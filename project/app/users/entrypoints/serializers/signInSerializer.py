from marshmallow import Schema, fields

class SignInSerializer(Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=False)
    professor_id = fields.Integer(required=False)
