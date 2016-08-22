class Question(BaseModel):
    content = CharField()
    status = CharField(default="New")
    time = DateTimeField()
    applicant = ForeignKeyField(Applicant, related_name="applicant_questions", null=True)
