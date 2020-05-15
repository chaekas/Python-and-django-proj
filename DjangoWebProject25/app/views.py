"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404
from app.forms import PostForm


from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import Post
from app.forms import PostForm


def Post_create(request):
    form = PostForm
    context = {
        'form': form,
        }

   
    return render(request, "app/form_detail.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
        }
    return render(request, "app/post_detail.html", context)

def index(request):
    queryset = Post.objects.order_by('-updated')
     # comments = comment.objects.order_by('-added_date')
    context = {
        "object_list": queryset,
        "title": "List"
        }
    return render(request, "app/index.html", context)



#def home(request):
    """Renders the home page."""
   # assert isinstance(request, HttpRequest)
    #return render(
        #request,
       # 'app/index.html',
       # {
            #'title':'Home Page',
           # 'year':datetime.now().year,
       # }
   # )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Maelezo',
            'message':'Maelezo kuhusu Blog.',
            'year':datetime.now().year,
        }
    )
