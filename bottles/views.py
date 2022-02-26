from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Letter
from .forms import ReplyForm
import random

letters = [{"author":"mwalklot0","body":"Sed ante. Vivamus tortor. Duis mattis egestas metus.\n\nAenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.","created_on":"12/17/2021"},
{"author":"varmitt1","body":"Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.\n\nVestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.\n\nIn congue. Etiam justo. Etiam pretium iaculis justo.","created_on":"6/22/2021"},
{"author":"svasyuchov2","body":"Duis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.\n\nMauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.","created_on":"11/13/2021"},
{"author":"llembrick3","body":"Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.","created_on":"2/6/2022"},
{"author":"mchalliner4","body":"Donec diam neque, vestibulum eget, vulputate ut, ultrices vel, augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec pharetra, magna vestibulum aliquet ultrices, erat tortor sollicitudin mi, sit amet lobortis sapien sapien non mi. Integer ac neque.\n\nDuis bibendum. Morbi non quam nec dui luctus rutrum. Nulla tellus.","created_on":"4/8/2021"},
{"author":"dmacsporran5","body":"Phasellus in felis. Donec semper sapien a libero. Nam dui.","created_on":"11/15/2021"},
{"author":"gsholl6","body":"Phasellus in felis. Donec semper sapien a libero. Nam dui.","created_on":"4/8/2021"},
{"author":"wtuckerman7","body":"In congue. Etiam justo. Etiam pretium iaculis justo.\n\nIn hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.\n\nNulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.","created_on":"9/16/2021"},
{"author":"thamal8","body":"Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.\n\nIn congue. Etiam justo. Etiam pretium iaculis justo.","created_on":"8/18/2021"},
{"author":"fgosford9","body":"Nulla ut erat id mauris vulputate elementum. Nullam varius. Nulla facilisi.\n\nCras non velit nec nisi vulputate nonummy. Maecenas tincidunt lacus at velit. Vivamus vel nulla eget eros elementum pellentesque.","created_on":"5/5/2021"},
{"author":"ggiacomuzzoa","body":"In hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.","created_on":"11/6/2021"},
{"author":"smcmeekingb","body":"Vestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.","created_on":"3/3/2021"},
{"author":"avasichevc","body":"Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis.\n\nDuis consequat dui nec nisi volutpat eleifend. Donec ut dolor. Morbi vel lectus in quam fringilla rhoncus.\n\nMauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.","created_on":"3/25/2021"},
{"author":"ymullengerd","body":"In congue. Etiam justo. Etiam pretium iaculis justo.\n\nIn hac habitasse platea dictumst. Etiam faucibus cursus urna. Ut tellus.","created_on":"6/27/2021"},
{"author":"dplaile","body":"Praesent blandit. Nam nulla. Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede.","created_on":"10/5/2021"},
{"author":"batackf","body":"Phasellus in felis. Donec semper sapien a libero. Nam dui.\n\nProin leo odio, porttitor id, consequat in, consequat ut, nulla. Sed accumsan felis. Ut at dolor quis odio consequat varius.","created_on":"9/30/2021"},
{"author":"xstanmoreg","body":"Quisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.\n\nVestibulum ac est lacinia nisi venenatis tristique. Fusce congue, diam id ornare imperdiet, sapien urna pretium nisl, ut volutpat sapien arcu sed augue. Aliquam erat volutpat.\n\nIn congue. Etiam justo. Etiam pretium iaculis justo.","created_on":"1/4/2022"},
{"author":"schasemoreh","body":"Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.\n\nPraesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio.","created_on":"1/13/2022"},
{"author":"lpringeri","body":"Mauris enim leo, rhoncus sed, vestibulum sit amet, cursus id, turpis. Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero.\n\nNullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh.","created_on":"10/18/2021"},
{"author":"kjoselevitzj","body":"Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh.\n\nQuisque id justo sit amet sapien dignissim vestibulum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros.","created_on":"12/1/2021"}]


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

