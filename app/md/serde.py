from marshmallow import fields,Schema

class NotesSchema(Schema):
    id=fields.Int(dump_only=True)
    data=fields.Str()
    date=fields.DateTime()
    user_id=fields.Int()