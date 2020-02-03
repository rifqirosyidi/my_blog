from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'my_blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'my_blog/about.html', context)