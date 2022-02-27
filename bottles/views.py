from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Letter
from .forms import ReplyForm
import random

class LetterList(generic.ListView):
    """
    docstring
    """
    model = Letter
    # queryset = Letter.objects.order_by("-created_on")
    template_name = "bottles/ocean.html"

    def get_context_data(self, **kwargs):
        context = super(LetterList, self).get_context_data(**kwargs)
        letters_list = Letter.objects.exclude(author=self.request.user)
        letters_obj = random.sample(list(letters_list), len(letters_list))
        try:
            letters_obj = random.sample(list(letters_list), 20)
            context['group_a'] = letters_obj[:5]
            context['group_b'] = letters_obj[5:10]
            context['group_c'] = letters_obj[10:15]
            context['group_d'] = letters_obj[15:20]
        except ValueError as e:
            letters_obj = random.sample(list(letters_list), len(letters_list))
            context['group_a'] = letters_obj[:5]
            context['group_b'] = letters_obj[5:10]
            context['group_c'] = letters_obj[10:15]
            context['group_d'] = letters_obj[15:20]
        return context


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
        letter.has_unseen_reply = False
        letter.save()
        replys = letter.replys.order_by("-created_on")  # oldest first
        return render(
            request,
            "bottles/letter_detail.html",
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
            letter.has_unseen_reply = True
            if letter.has_reply is False:
                letter.has_reply = True
            letter.save()
        else:
            reply_form = ReplyForm()
            letter.has_unseen_reply = False 
            letter.save()
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
   