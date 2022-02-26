from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Letter
from .forms import ReplyForm
import random

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
{"first_name":"Dory","last_name":"Goring","email":"dgoringo@163.com","gender":"Female","bottle":"Roses are red, violets are blue","answer":"A sun is bright, and so are you."},
{"bottle":"Orchids are white, ghost ones are rare","answer":"Days are golden, and so is your hair."},
{"bottle":"Magnolia grows, with buds like eggs","answer":"The air is thin, and so are your legs."},
{"bottle":"Sunflowers reach, up to the skies,","answer":"The brown is pale, and so are your eyes."},
{"bottle":"Foxgloves in hedges, surround the farms,","answer":"My story is short, and so are your arms."},
{"bottle":"Daisies are pretty, daffies have style,","answer":"Purposes are illuminating, and so is your smile."}]


def ocean(request):
    """ docstring """
    if request.method == 'GET':
        random.shuffle(letters)
        group_a = letters[:5]
        group_b = letters[5:10]
        group_c = letters[10:15]
        context = {'group_a': group_a, 'group_b': group_b, 'group_c': group_c }
        return render(request, 'bottles/ocean.html', context)
    
    

class LetterList(generic.ListView):
    """
    docstring
    """
    model = Letter
    queryset = Letter.objects.order_by("-created_on")
    template_name = "home/landing.html"


class LetterDetail(View):
    """
    A view to show 5 lastest letters ordered by created
    Args:
        ListView: class based view
    Returns:
        Render of home page with context
    """
    def get(self, request, slug):
        """
        doc string
        """
        queryset = Letter.objects
        letter = get_object_or_404(queryset, slug=slug)
        replys = letter.replys.order_by("-created_on")  # oldest first
        return render(
            request,
            "home/landing_detail.html",
            {
                "letter": letter,
                "replys": replys,
                "reply_form": ReplyForm(),

            },
        )

    def post(self, request, slug):
        """
        doc string
        """
        queryset = Letter.objects
        letter = get_object_or_404(queryset, slug=slug)
        replys = letter.replys.order_by("-created_on")  # oldest first
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():
            reply_form.instance.name = request.user.username
            reply_form.instance.email = request.user.email
            reply = reply_form.save(commit=False)
            reply.letter = letter
            reply.save()
        else:
            reply_form = ReplyForm()
        return render(
            request, "home/landing_detail.html",
            {
                "letter": letter,
                "replys": replys,
                "reply_form": ReplyForm(),
                },
        )

@login_required
def ContactView(request, slug):
    """
    Sends email -contact us form fields to admin or prints to the terminal
    in development
    Prepopulates email and username
    Args:
       request (object): HTTP request object.
       slug: slug
    Returns:
       Render contact us page  with context
    """
    email = request.user.email
    username = request.user.username

    queryset = Letter.objects
    letter = get_object_or_404(queryset, slug=slug)
    replys = letter.replys.order_by("-created_on") 
    
    if request.method == "POST":
        message_subject_a = request.POST['message-subject-display']
        message_email = request.POST['message-email']
   
        message_body = request.POST['message']
        send_mail(
            message_subject_a,
            message_body,
            email, #users email
            [message_email], #person that wrote the replys email
        )
        # messages.success(request, 'Email sent successfully')
    return render(request, 'bottles/contact.html',  {'slug': slug, 'email': email, 'replys': replys, 'username':username})
   