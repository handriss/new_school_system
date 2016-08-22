class InterviewSlot(BaseModel):
    start = DateTimeField()
    end = DateTimeField()
    reserved = BooleanField(default=False)
    school = ForeignKeyField(School, related_name="interviewslots", null=True)
    mentor_one = ForeignKeyField(Mentor, null=True, related_name="interviewslot_1")
    mentor_two = ForeignKeyField(Mentor, null=True, related_name="interviewslot_2")
