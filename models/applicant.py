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

    @classmethod
    def new_applicant(cls, dictionary):
        cls.create(**dictionary)

    @classmethod
    def all_applicant(cls):
        query = cls.select(cls.first_name, cls.last_name, cls.email, cls.city, cls.application_code
                                , cls.status, School.city).join(School, JOIN.LEFT_OUTER)
        return query


