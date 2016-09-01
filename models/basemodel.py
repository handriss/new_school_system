from peewee import *
import getpass


db = PostgresqlDatabase(str(getpass.getuser()), user=str(getpass.getuser()))


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    @classmethod
    def get_model_attributes(cls):
        """ Returns the model's attributes
        :returns: list -- a list of strings of the attributes
        """
        return cls._meta.sorted_field_names

    class Meta:
        database = db
