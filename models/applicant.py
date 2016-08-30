from models.basemodel import BaseModel
from peewee import *
from models.school import School
from models.interviewslot import InterviewSlot


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    city = CharField()
    application_code = CharField(null=True)
    status = CharField(default='New applicant')
    school = ForeignKeyField(School, related_name='applicant', null=True)
    interviewslot = ForeignKeyField(InterviewSlot, null=True, related_name='applicants')

    def new_applicant(self, dictionary):
        with db.atomic():
            Applicant.insert_many(dictionary).execute()

    def all_applicant(self):
        return Applicant.select(Applicant.first_name, Applicant.last_name)