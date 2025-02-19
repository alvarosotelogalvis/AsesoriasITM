from marshmallow import Schema, fields

class UpdateScheduleSchema(Schema):
    group_id = fields.String(required=True)
    subject = fields.String(required=False)
    schedule = fields.String(required=False)
    classroom = fields.String(required=False)
    academic_program = fields.String(required=False)
