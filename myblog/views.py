from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
import markdown


# Create your views here.
def home(request):
    post_list = Post.objects.all()
    tag_list = Tag.objects.all()
    context = {
        'post_list': post_list,
        'tag_list': tag_list,
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                  ])
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def about(request):
    return render(request, 'about.html')
