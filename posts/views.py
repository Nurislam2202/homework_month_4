from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def hello_view(request):
    return HttpResponse('How are you bro?')


def html_view(request):
    return render(request, 'base.html')


def list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_view.html', context={"posts": posts})
