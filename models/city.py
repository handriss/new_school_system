from models.basemodel import BaseModel
from peewee import *


class City(BaseModel):
    city = CharField()
    school_city = CharField()
