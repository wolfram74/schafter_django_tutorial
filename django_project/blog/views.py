from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import time
import datetime

posts = Post.objects.all()

def home(request):
    context = {
        'posts':posts
    }
    print(str(posts.first().date_posted))
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
