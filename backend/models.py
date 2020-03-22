import peewee as p
from datetime import datetime

db = p.SqliteDatabase('database.sql')


class BaseModel(p.Model):
    class Meta:
        database = db


class User(BaseModel):
    """ Our user's information, i.e. telephone guy """
    username = p.CharField(unique=True)
    password = p.CharField()
    firstname = p.CharField()
    lastname = p.CharField()
    phone = p.CharField()


class Customer(BaseModel):
    """ Store our customer here """
    firstname = p.CharField()
    lastname = p.CharField()
    phone = p.CharField()
    location = p.CharField()

    def add_job(self, **kwargs):
        """ Proxy `Job` properties and automatically associate customer """
        job = Job(customer=self, **kwargs)
        job.save()

        return job


class Platform(BaseModel):
    """ Helper Platform """
    # Used for easier reference during input and coding
    shortname = p.CharField(unique=True)
    # Full name
    name = p.CharField()
    url = p.CharField()

    # Be ugly: Just use commas to seperate information...
    locations = p.TextField()
    jobtypes = p.TextField()


class Helper(BaseModel):
    """ External helper associated with platform """
    firstname = p.CharField()
    lastname = p.CharField()

    # Phone or email address
    contact = p.CharField()

    platform = p.ForeignKeyField(Platform, backref="helpers")


class Job(BaseModel):
    """ Store information about Customer's job inquiry """
    customer = p.ForeignKeyField(Customer, backref="jobs")

    jobtype = p.CharField()  # Restrict types with dropdown field?
    requested_time = p.DateTimeField()
    description = p.TextField(null=True)

    # Allow null because `Helper` information are associated after job creation.
    helper = p.ForeignKeyField(Helper, backref="jobs", null=True)

    # Status. Did `Helper` accept and finish job?
    accepted = p.BooleanField(default=False)
    finished = p.BooleanField(default=False)


def setup(example=False):
    if example:
        db.init(":memory:")

    with db:
        db.create_tables([User, Customer, Job, Platform, Helper])

        if example:
            # Create dummy user
            user = User(username="jdoe", password="plain", firstname="John", lastname="Doe", phone="110")
            user.save()

            # Create dummy customer
            erna = Customer(firstname="Erna", lastname="Müller", phone="112", location="Braunschweig")
            erna.save()

            # Create Erna's job, saving is done automatically but we can save manually again
            job = erna.add_job(jobtype="Einkaufen", requested_time=datetime(2020, 3, 22, 15, 20, 0))
            job.save()

            # Create platform
            sandkasten = Platform(shortname="sandkasten", name="Sandkasten Projekt", url="sandkasten.de", locations="Braunschweig, Wolfsburg", jobtypes="Einkauf")
            sandkasten.save()

            # Create Helper
            caro = Helper(firstname="Caro", lastname="Helfer", contact="caro@helfer.de", platform=sandkasten)
            caro.save()

            # Check caros job count
            print("Caro has {:d} jobs to do".format(caro.jobs.count()))

            # Associate Caro to Erna's job
            job.helper = caro
            job.save()

            # Check if Caro has a new job:
            for j in caro.jobs:
                print("Job #{:d} for {:s}".format(j.id, j.customer.firstname))

            # Check caros job count, again
            print("Caro has {:d} jobs to do".format(caro.jobs.count()))


if __name__ == '__main__':
    setup(example=True)
