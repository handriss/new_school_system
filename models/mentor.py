class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    school = ForeignKeyField(School, related_name="mentor", null=True)
