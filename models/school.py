from models.basemodel import BaseModel
from peewee import *


class School(BaseModel):
    city = CharField()
