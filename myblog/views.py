from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
from django.core.paginator import Paginator
import markdown


# Create your views here.
def home(request):
    post_list = Post.objects.all()
    date_list = Post.objects.dates('created_time', 'month', order='DESC')
    tag_list = Tag.objects.all()
    paginator = Paginator(post_list, 10)  # Show 10 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'date_list': date_list,
        'tag_list': tag_list,
        'page_obj': page_obj,
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.blog_views = post.blog_views+1
    post.save()
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


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month)
    date_list = Post.objects.dates('created_time', 'month', order='DESC')
    tag_list = Tag.objects.all()
    paginator = Paginator(post_list, 5)  # Show 5 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'date_list': date_list,
        'tag_list': tag_list,
        'page_obj': page_obj,
    }
    return render(request, 'home.html', context)


def tag(request, tag_pk):
    post_list = Post.objects.filter(tags=tag_pk).order_by('-created_time')
    date_list = Post.objects.dates('created_time', 'month', order='DESC')
    tag_list = Tag.objects.all()
    paginator = Paginator(post_list, 5)  # Show 5 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
        'date_list': date_list,
        'tag_list': tag_list,
        'page_obj': page_obj,
    }
    return render(request, 'home.html', context)
