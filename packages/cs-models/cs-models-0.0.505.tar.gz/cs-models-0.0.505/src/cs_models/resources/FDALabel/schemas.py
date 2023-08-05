from marshmallow import (
    Schema,
    fields,
    validate,
)


class FDALabelResourceSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)
    set_id = fields.String(required=True)
    doc_id = fields.String(required=True)
    date = fields.DateTime(required=True)
    version = fields.String(required=True)
    section_id = fields.String(required=True)
    section_text = fields.String(allow_none=True)
    section_html_file_id = fields.Integer(required=True)
    label_html_file_id = fields.Integer(required=True)
    updated_at = fields.DateTime(dump_only=True)
