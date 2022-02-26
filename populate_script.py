# import os, django 

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'message_in_a_bottle.settings')

# django.setup()

# from faker import Faker
# from django.contrib.auth.models import User 

# def create_user(N):
#     fake = Faker()
#     for _ in range(N):
#         name=fake.name()
#         f_name = name.split(' ')[0]
#         l_name = name.split(' ')[1]
#         username = fake.user_name()
#         email = fake.email()
#         password = fake.password()
#         User.objects.create_user(username=username, email=email, password=password, first_name=f_name, last_name=l_name)
# create_user()


# id, author, body, slug, Letter.create(author=(User.objects.get(id=id), body=.......))

