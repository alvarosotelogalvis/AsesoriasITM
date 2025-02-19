from marshmallow import Schema, fields

class DeleteScheduleSchema(Schema):
    group_id = fields.String(required=True)
