from faker import Faker
import random



def FakePerson():
    person = {}
    fake = Faker()
    fakeSeed = random.randrange(1,100000)

    fake.seed_instance(fakeSeed)
    
    fakeName = fake.name()
    fakeIP = fake.ipv4_private()
    fakeJob = fake.job()
    fakeCompany = fake.company()
    person = {"name": fakeName, "IP": fakeIP, "Job" : fakeJob, "Company": fakeCompany}
    return person

if __name__ == "__main__":
    print(FakePerson())
