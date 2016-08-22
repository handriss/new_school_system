class Answer(BaseModel):
    content = CharField()
    mentor = ForeignKeyField(Mentor, related_name="answers", null=True)
    question = ForeignKeyField(Question, related_name="related_answer", null=True)
