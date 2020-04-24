from django.shortcuts import render, redirect
from .models import Post, Comment, Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import RedirectView
# Create your views here.

# View individual post with comments
def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("ERROR 404: Post does not exist")
    comments = post.comment_set.order_by('-pub_date')
    return render(request, 'post/post_view.html', {'post': post, 'comments': comments})

# Home page 
def home(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request,'post/home.html',{'posts':posts})

# PostLike View
def post_like(request): 
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=post_id)
        likers = post.postlike.likers.all()
        user = request.user
        if user in likers:
            post.postlike.likers.remove(user)
        else:
            post.postlike.likers.add(user)
        return HttpResponse('success')
    else:
        return HttpResponse('fail')

