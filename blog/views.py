from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'ShahriyarHossain',
        'title': 'Blog Post 1',
        'content': 'First post contents are here!',
        'date_posted': 'January 20, 2020'
    },
    {
        'author': 'ShonaK',
        'title': 'Blog Post 2',
        'content': '2nd post contents are here!',
        'date_posted': 'January 19, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
# Create your views here.
