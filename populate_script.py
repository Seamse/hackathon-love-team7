import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'message_in_a_bottle.settings')

django.setup()

from faker import Faker
from django.contrib.auth.models import User 
from bottles.models import Letter
from django.utils import timezone
from django.utils.crypto import get_random_string

def create_user(N):
    fake = Faker()
    for _ in range(N):
        name=fake.name()
        f_name = name.split(' ')[0]
        l_name = name.split(' ')[1]
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        User.objects.create_user(username=username, email=email, password=password, first_name=f_name, last_name=l_name)

# create_user()

def create_letter(N):
    fake = Faker()
    for _ in range(N):
        id = random.randint(1, len(User.objects.all()))
        author = User.objects.get(id=id)
        body = fake.text(max_nb_chars=100)
        created = timezone.now()
        slug = get_random_string(12, '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        Letter.objects.create(body=body, slug=slug, author=author, created_on=created )

create_letter(50)




