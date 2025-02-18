from marshmallow import Schema, fields

class SignUpSchema(Schema):
    institutional_email = fields.String(required=True)
    identification_card = fields.Integer(required=True)
    password = fields.String(required=True)
