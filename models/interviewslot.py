from models.basemodel import BaseModel
from peewee import *
from models.school import School
from models.mentor import Mentor


class InterviewSlot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField(default=False)
    school = ForeignKeyField(School, related_name="interviewslots", null=True)
    mentor_one = ForeignKeyField(Mentor, null=True, related_name="interviewslot_1")
    mentor_two = ForeignKeyField(Mentor, null=True, related_name="interviewslot_2")
