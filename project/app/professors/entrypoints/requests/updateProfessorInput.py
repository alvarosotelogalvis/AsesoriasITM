from marshmallow import Schema, fields

class UpdateprofessorSchema(Schema):
    fullname = fields.String(required=False)
    identification_card = fields.Integer(required=True)
    department = fields.String(required=False)
    program = fields.String(required=False)
    highest_education_level = fields.String(required=False)
    degree_obtained = fields.String(required=False)
    undergraduate_degree = fields.String(required=False)
    partnership = fields.String(required=False)
    institutional_email = fields.String(required=False)
    personal_email = fields.String(required=False)
    email_with_domain = fields.String(required=False)
    faculty_location = fields.String(required=False)
