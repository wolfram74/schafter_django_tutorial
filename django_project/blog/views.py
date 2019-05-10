from django.shortcuts import render
from django.http import HttpResponse
import time
import datetime

today = datetime.date.today()
yesterday = today + datetime.timedelta(days=-1)
posts = [
    {
        'author':'perp1',
        'title':'bost plog 1',
        'content':'fumble buckets',
        'date_posted':today,
    },
    {
        'author':'perp2',
        'title':'bost plog 4',
        'content':'fumble truckets',
        'date_posted':yesterday,
    },
]


def home(request):
    context = {
        'posts':posts
    }
    print(str(posts[0]['date_posted']))
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
