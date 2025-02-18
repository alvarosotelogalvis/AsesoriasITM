from marshmallow import Schema, fields

class GetAllScheduleSchema(Schema):
    page = fields.Integer(required=True)
    per_page = fields.Integer(required=True)
