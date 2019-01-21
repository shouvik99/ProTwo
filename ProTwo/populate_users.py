import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'ProTwo.settings')


import django
django.setup()

from AppTwo.models import User
from faker import Faker 

fakeusers = Faker()

def populate(N=5):
    
    
    for entry in range(N):
        fake_name = fakeusers.name(),split()
        fake_first_name = fake_name[0] 
        fake_last_name = fake_name[1]
        fake_email = fakeusers.email()


        #New entry
        user = user.objects.get_or_create(first_name= fake_first_name,
                                          last_name = fake_last_name,
                                          email = fake_email)[0]

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(20)
    print("COMPLETE")


    ###  THIS IS NOT WORKING, I DON'T KNOW WHY!! 