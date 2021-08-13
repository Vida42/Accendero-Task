from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

# Create your views here.
def index(request):
    context = {
        'title': 'MyBlog',
        'word': "Welcome To My Blog!"
    }
    return render(request, 'home.html', context)
