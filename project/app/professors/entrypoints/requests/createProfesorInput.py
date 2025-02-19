from marshmallow import Schema, fields

class CreateprofessorSchema(Schema):
    fullname = fields.String(required=True)
    identification_card = fields.Integer(required=True)
    department = fields.String(required=True)
    program = fields.String(required=True)
    highest_education_level = fields.String(required=True)
    degree_obtained = fields.String(required=True)
    undergraduate_degree = fields.String(required=True)
    partnership = fields.String(required=True)
    institutional_email = fields.String(required=True)
    personal_email = fields.String(required=True)
    email_with_domain = fields.String(required=True)
    faculty_location = fields.String(required=True)
    role = fields.String(required=True)
