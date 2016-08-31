from models.basemodel import BaseModel
from peewee import *
from models.school import School
from models.interviewslot import InterviewSlot
import random
import string


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
    def get_application_codes(cls):
        """ Saves to the class and returns all application codes of the applicants. """
        cls.application_codes = [applicant.application_code for applicant in Applicant.select()]
        return cls.application_codes

    @classmethod
    def application_code_generator(cls):
        """ Generates a new, random, six-digit application code that is unique to other application codes. """
        application_code = (''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6)))
        while application_code in cls.application_codes:
            application_code = (''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6)))
        return application_code
