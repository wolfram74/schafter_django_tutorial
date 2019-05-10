from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.

def home(request):
    template = '''
    <h1>blog home</h1>
    <br>
    <h2> %d </h2>
    '''

    return HttpResponse(
        template % time.time()
        )

def about(request):
    template = '''
    <h1>blog about</h1>
    <br>
    <h2> %d </h2>
    <p>we're all pickles with anxiety</p>
    '''
    return HttpResponse(
        template % time.time()
        )
