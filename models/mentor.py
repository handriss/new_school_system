from models.basemodel import BaseModel
from peewee import *
from models.school import School


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    password = CharField()
    school = ForeignKeyField(School, related_name="mentor", null=True)
