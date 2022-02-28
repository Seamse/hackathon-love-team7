from django.shortcuts import render, get_object_or_404
from bottles.models import Letter, Reply
from .models import Profile
from .forms import ProfileForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

@login_required
def profiles(request):
    """
    dlkcvjadl
    """
    model = Profile
    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=profile)


    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template, context)


class inbox(LoginRequiredMixin, generic.ListView):
    """
    docstring
    """
    model = Letter

    template_name = "profiles/inbox.html"

    def get_context_data(self, **kwargs):
        context = super(inbox, self).get_context_data(**kwargs)
        user_letter_list = Letter.objects.filter(author=self.request.user)
        unreplied_letters = user_letter_list.filter(has_reply=False)
        letter_with_unseen_reply = user_letter_list.filter(has_unseen_reply=True)
        letter_with_seen_reply = user_letter_list.filter(has_unseen_reply=False).filter(has_reply=True)
        user_reply_list = Reply.objects.filter(name=self.request.user)
        # user_reply_list
        context['unreplied_letters'] = unreplied_letters
        context['letter_with_unseen_reply'] = letter_with_unseen_reply
        context['letter_with_seen_reply'] = letter_with_seen_reply
        context['replys'] = user_reply_list
        return context 

class InboxDetail(LoginRequiredMixin, View):
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
            "profiles/inbox_detail.html",
            {
                "letter": letter,
                "replys": replys,
            

            },
        )
