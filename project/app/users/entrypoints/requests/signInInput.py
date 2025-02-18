from marshmallow import Schema, fields

class SignInSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
