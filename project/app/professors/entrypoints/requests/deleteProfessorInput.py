from marshmallow import Schema, fields

class DeleteprofessorSchema(Schema):
    identification_card = fields.Integer(required=True)
