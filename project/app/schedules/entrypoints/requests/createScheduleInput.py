from marshmallow import Schema, fields

class CreateScheduleSchema(Schema):
    group_id = fields.String(required=True)
    subject = fields.String(required=True)
    schedule = fields.String(required=True)
    classroom = fields.String(required=True)
    academic_program = fields.String(required=True)
