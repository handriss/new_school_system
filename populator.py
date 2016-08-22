from models import *
from datetime import *
from random import randint
import psycopg2
import smtplib


class Populator():

    @staticmethod
    def establish_connection():
        """ Connects to the database and creates the necessary tables. """
        db.connect()
        db.drop_tables([Question, InterviewSlot, School, Applicant, City, Mentor], safe=True)
        db.create_tables([Question, InterviewSlot, School, Applicant, City, Mentor], safe=True)

    @staticmethod
    def populate_tables():
        """ Populates the tables with the example data. """
        cities, applicants, mentors, interview_slots, questions = Populator.example_data()

        with db.atomic():
            City.insert_many(cities).execute()
            Applicant.insert_many(applicants).execute()
            Mentor.insert_many(mentors).execute()
            InterviewSlot.insert_many(interview_slots).execute()
            Question.insert_many(questions).execute()

    @staticmethod
    def example_data():
        """ Contains the example data for populating the tables in the database. """

        questions = [
            {"content": "Who are those horrible orange creatures over there?", "applicant": 1,
                "time": datetime(2016, 8, 16, 7, 12)},
            {"content": "Wow, your kid's really good. How hard do you have to hit him?", "applicant": 1,
                "time": datetime(2016, 7, 20, 11, 32)},
            {"content": "Is it just coincidence that Zoidberg is poor and miserably lonely?", "applicant": 2,
                "time": datetime(2016, 8, 21, 11, 56)},
            {"content": "What makes a good man go neutral?", "applicant": 3,
                "time": datetime(2016, 8, 11, 18, 21)},
            {"content": "Did everything just taste purple?", "applicant": 5,
                "time": datetime(2016, 8, 10, 19, 51)},
            {"content": "Do you see a robot in this room named Folder?", "applicant": 8,
                "time": datetime(2016, 7, 15, 23, 38)}
        ]

        interview_slots = [
            {"start": datetime(2016, 8, 15, 10, 0), "end": datetime(2016, 8, 15, 11, 0), "mentor": 1, "school_id": 1},
            {"start": datetime(2016, 8, 15, 13, 0), "end": datetime(2016, 8, 15, 14, 0), "mentor": 2, "school_id": 1},
            {"start": datetime(2016, 8, 15, 15, 0), "end": datetime(2016, 8, 15, 16, 0), "mentor": 1, "school_id": 1},
            {"start": datetime(2016, 8, 16, 10, 0), "end": datetime(2016, 8, 16, 11, 0), "mentor": 2, "school_id": 1},
            {"start": datetime(2016, 8, 16, 13, 0), "end": datetime(2016, 8, 16, 14, 0), "mentor": 1, "school_id": 1},
            {"start": datetime(2016, 8, 16, 15, 0), "end": datetime(2016, 8, 16, 16, 0), "mentor": 2, "school_id": 1},
            {"start": datetime(2016, 8, 16, 15, 0), "end": datetime(2016, 8, 16, 16, 0), "mentor": 1, "school_id": 1},
            {"start": datetime(2016, 8, 17, 10, 0), "end": datetime(2016, 8, 17, 11, 0), "mentor": 3, "school_id": 2},
            {"start": datetime(2016, 8, 17, 13, 0), "end": datetime(2016, 8, 17, 14, 0), "mentor": 4, "school_id": 2},
            {"start": datetime(2016, 8, 17, 15, 0), "end": datetime(2016, 8, 17, 16, 0), "mentor": 3, "school_id": 2},
            {"start": datetime(2016, 8, 18, 10, 0), "end": datetime(2016, 8, 18, 11, 0), "mentor": 4, "school_id": 2},
            {"start": datetime(2016, 8, 18, 13, 0), "end": datetime(2016, 8, 18, 14, 0), "mentor": 3, "school_id": 2},
            {"start": datetime(2016, 8, 19, 10, 0), "end": datetime(2016, 8, 19, 11, 0), "mentor": 4, "school_id": 2},
            {"start": datetime(2016, 8, 19, 13, 0), "end": datetime(2016, 8, 19, 14, 0), "mentor": 3, "school_id": 2}

        ]

        cities = [
            {"city": "Érd", "school_city": "Budapest"},
            {"city": "Kiskunbüdösbütykös", "school_city": "Miskolc"},
            {"city": "Mars", "school_city": "Miskolc"},
            {"city": "Tijuana", "school_city": "Budapest"},
            {"city": "Decapod 10", "school_city": "Miskolc"},
            {"city": "Nimbus", "school_city": "Budapest"},
            {"city": "New New York", "school_city": "Budapest"}
        ]

        bp = School.create(city="Budapest")
        miskolc = School.create(city="Miskolc")
        krakow = School.create(city="Krakow")

        applicants = [
            {"first_name": "Jack", "last_name": "Johnson", "email": "jackjohnson@gmail.com",
                "city": "Érd", "application_code": "GFJEDF", "school": bp},
            {"first_name": "John", "last_name": "Jackson", "email": "johnjackson@gmail.com",
                "city": "Kiskunbüdösbütykös", "application_code": None, "school": None},
            {"first_name": "Amy", "last_name": "Wong", "email": "awong79@marslink.web",
                "city": "Mars", "application_code": None, "school": None},
            {"first_name": "Bender", "last_name": "Rodriguez", "email": "bender@ilovebender.com",
                "city": "Tijuana", "application_code": None, "school": None},
            {"first_name": "John", "last_name": "Zoidberg", "email": "zoidberg@decapodians.deca",
                "city": "Decapod 10", "application_code": None, "school": None},
            {"first_name": "Kif", "last_name": "Kroker", "email": "iamgreen@military.earth",
                "city": "Nimbus", "application_code": None, "school": None},
            {"first_name": "Zapp", "last_name": "Brannigan", "email": "lovethezapper@military.earth",
                "city": "Nimbus", "application_code": None, "school": None},
            {"first_name": "Hermes", "last_name": "Conrad", "email": "bureaucrat_conrad@gmail.com",
                "city": "New New York", "application_code": None, "school": None},
            {"first_name": "Antonio", "last_name": "Calculon", "email": "allmycircuits@gmail.com",
                "city": "New New York", "application_code": None, "school": None},
            {"first_name": "Philip", "last_name": "Fry", "email": "iloveleela@gmail.com", "city":
                "New New York", "application_code": None, "school": None}
        ]

        mentors = [
            {"first_name": "Hubert", "last_name": "Farnsworth", "email": "", "school": bp},
            {"first_name": "Morbo", "last_name": "the Annihilator", "email": "iwilldestroyyou@gmail.com", "school": bp},
            {"first_name": "Lord", "last_name": "Nibbler", "email": "iamcute@nibblonians.niblo", "school": miskolc},
            {"first_name": "Richard", "last_name": "Nixon", "email": "nixonalwayswins@head.gov", "school": miskolc}
        ]

        return cities, applicants, mentors, interview_slots, questions

    @staticmethod
    def run_sql(query):
        try:
            conn = psycopg2.connect(dbname=str(getpass.getuser()), user=str(getpass.getuser()))
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Uh oh, can't connect. Invalid dbname, user or password?")
            print(e)


class Email():

    @staticmethod
    def send_email(user, pwd, recipient, subject, body):

        gmail_user = user
        gmail_pwd = pwd
        FROM = user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")
