from marshmallow import fields,Schema

class UsersSchema(Schema):
    id=fields.Int(dump_only=True)
    username=fields.Str()
    email=fields.Str()
    password=fields.Str(load_only=True)
