from models.basemodel import BaseModel
from peewee import *
from models.school import School
from models.interviewslot import InterviewSlot
from models.city import City



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



    @classmethod
    def run_query(cls, filter_by, value):

        # mentor query for the future

        # if filter_by == "mentor":
        #     query = []
        #     for applicant in Applicant.select():
        #         if applicant.interview.mentor.first_name.contains(value):
        #             query.append([applicant.first_name, applicant.last_name, applicant.email, applicant.city])


        if filter_by == "school":
            query = Applicant.select(
                Applicant.first_name,
                Applicant.last_name,
                Applicant.email,
                Applicant.city
            ).join(City, JOIN.FULL, Applicant.city == City.city).where(City.school_city.contains(value))
        else:
            query = cls.select(cls.first_name,
                               cls.last_name,
                               cls.email,
                               cls.city,
                               cls.application_code,
                               School.city,
                               cls.status).join(School, JOIN.LEFT_OUTER).where(getattr(cls, filter_by).contains(value))

        return query
