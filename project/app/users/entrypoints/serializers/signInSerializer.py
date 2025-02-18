from marshmallow import Schema, fields

class SignInSerializer(Schema):
    id = fields.Integer(required=False)
    username = fields.String(required=False)
    profesor_id = fields.Integer(required=False)
