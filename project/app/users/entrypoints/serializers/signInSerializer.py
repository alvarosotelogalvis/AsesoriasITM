from marshmallow import Schema, fields

class SignInSerializer(Schema):
    id = fields.Integer(required=False)
    fullname = fields.String(required=False)
    role = fields.String(required=False)
