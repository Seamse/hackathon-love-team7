import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'message_in_a_bottle.settings')

django.setup()

from faker import Faker
from django.contrib.auth.models import User 
from bottles.models import Letter, Reply
from django.utils import timezone
from django.utils.crypto import get_random_string





letters = [{"bottle":"Foxgloves in hedges, surround the farms","answer":"A way is long and so are your arms."},
{"bottle":"Daisies are pretty, daffies have style,","answer":"The ticket is winning, and so is your smile."},
{"bottle":"A lily is beautiful","answer":"Just like you."},
{"bottle":"Roses are red, violets are blue,","answer":"The tale is weird, and so are you."},
{"bottle":"In summertime, our love is kind, like roses floating in the breeze.","answer":"In wintertime, our love is warm — it goes from arm to toes."},
{"bottle":"Roses are red, Violets are blue","answer":"shoes are cute, and so are you."},
{"bottle":"Orchids are white, ghost ones are rare","answer":"A dress is black, and so is your hair."},
{"bottle":"Magnolia grows, with buds like eggs","answer":"Your yellow is pale, and so are your legs."},
{"bottle":"Sunflowers reach, up to the skies","answer":"The sky is pale, and so are your eyes."},
{"bottle":"If skies are blue, our love is happy — two people dancing in the sun.","answer":"If thunder rolls our love is calm, a refuge from the falling rain."},
{"bottle":"I don't like short poems. So why am I reviewing a haiku, you may wonder?","answer":"Well, I liked the title - 'Snail'. It went down hill from there."},
{"bottle":"Roses are red, violets are blue","answer":"This website is weird, and so are you."},
{"bottle":"Orchids are white, ghost ones are rare","answer":"My history is long, and so is your hair."},
{"bottle":"Magnolia grows with buds like eggs","answer":"Your film is thin, and so are your legs."},
{"bottle":"Sunflowers reach up to the skies","answer":"Treatment is kind, and so are your eyes."},
{"bottle":"Foxgloves in hedges, surround the farms","answer":"My intake is fat, and so are your arms."},
{"bottle":"Daisies are pretty, daffies have style","answer":"Your place is warm, and so is your smile."},
{"bottle":"Roses are red, violets are blue","answer":"The student is bright, and so are you."},
{"bottle":"Orchids are white, ghost ones are rare","answer":"Your mean is golden, and so is your hair."},
{"bottle":"Magnolia grows, with buds like eggs","answer":"A film is thin, and so are your legs."},
{"bottle":"Sunflowers reach, up to the skies","answer":"Pink is pale, and so are your eyes."},
{"bottle":"Foxgloves in hedges, surround the farms","answer":"Your supply is short, and so are your arms."},
{"bottle":"Daisies are pretty, daffies have style","answer":"The example is illuminating, and so is your smile."},
{"bottle":"A seahorse is beautiful","answer":"And so are you!"},
{"bottle":"Roses are red, violets are blue","answer":"A sun is bright, and so are you."},
{"bottle":"Orchids are white, ghost ones are rare","answer":"Days are golden, and so is your hair."},
{"bottle":"Magnolia grows, with buds like eggs","answer":"The air is thin, and so are your legs."},
{"bottle":"Sunflowers reach, up to the skies,","answer":"The brown is pale, and so are your eyes."},
{"bottle":"Foxgloves in hedges, surround the farms,","answer":"My story is short, and so are your arms."},
{"bottle":"Daisies are pretty, daffies have style,","answer":"Purposes are illuminating, and so is your smile."}]



# def create_letter(N):
#     fake = Faker()
#     for _ in range(N):
#         id = random.randint(1, len(User.objects.all()))
#         author = User.objects.get(id=id)
#         body = fake.text(max_nb_chars=100)
#         created = timezone.now()
#         slug = get_random_string(12, '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
#         Letter.objects.create(body=body, slug=slug, author=author, created_on=created )

# create_letter()


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




#def create_bottled_message(N=1):
#    for _ in range(N):
#        id = random.randint(1,5)
#        body = random.choice(letters).get('bottle')
#        author = User.objects.get(id=id)
#        slug = body.replace(' ','-').replace(',','').split(' ')[0]
#        letter = Letter(author=author,body=body,slug=slug)
#        letter.save()
        #Letter.objects.create(author=author,body=body,slug=slug)
        

#def create_answer_to_bottle(N=1):
#    for _ in range(N):
#        id = random.randint(1,5)
#        body = random.choice(letters).get('answer')
#        author = User.objects.get(id=id)
#        slug = body.replace(' ','-').replace(',','').split(' ')[0]
#        Reply.objects.create(author=author,body=body,slug=slug)

#create_bottled_message()