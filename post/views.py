from django.shortcuts import render, redirect
from .models import Post, Comment, PostLike
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import RedirectView
from django.utils import timezone
# Create your views here.

# View individual post with comments
def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("ERROR 404: Post does not exist")
    comments = post.comment_set.order_by('-pub_date')
    return render(request, 'post/post_view.html', {'post': post, 'comments': comments, 'title':'Post by '+post.author.username})

# Home page 
def home(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request,'post/home.html',{'posts':posts,'title':'Home'})

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

#Post Creation View
def post_create(request):
    if request.method == 'POST':
        post_text = request.POST['post_text']
        if len(post_text)>5000:
            messages.warning(request, f'Post exceeds character limit.')
            return redirect('home')
        for ch in post_text:
            if(ch.isalpha() or ch.isdigit()):
                new_post = Post(text=post_text, author=request.user, pub_date=timezone.now())
                new_post.save()
                new_post_likes = PostLike(parent_post=new_post)
                new_post_likes.save()
                messages.success(request, f'Post created successfully!')
                return redirect('home')
        messages.warning(request, f'Please enter content in your post.')
        return redirect('home')
    else:
        return redirect('home')

#Post Deletion View
def post_delete(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        if Post.objects.get(pk=post_id).author == request.user:
            post = Post.objects.get(id = post_id)
            post.delete()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
    else:
        return HttpResponse('fail')
        
#Comment Creation View
def comment_create(request):
    if request.method == 'POST':
        comment_text = request.POST['comment_text']
        post_id = request.POST['post']
        post = Post.objects.get(pk=post_id)
        if len(comment_text)>500:
            messages.warning(request, f'Comment exceeds character limit.')
            return redirect('post:post_view', post_id=post.id)
        for ch in comment_text:
            if(ch.isalpha() or ch.isdigit()):
                new_comment = Comment(parent_post=post, text=comment_text, author=request.user, pub_date=timezone.now())
                new_comment.save()
                messages.success(request, f'Comment added successfully!')
                return redirect('post:post_view', post_id=post.id)
        messages.warning(request, f'Please enter content in your comment.')
        return redirect('post:post_view', post_id=post.id)
    else:
        return redirect('home')

#Comment Deletion View
def comment_delete(request):
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
        if Comment.objects.get(pk=comment_id).author == request.user:
            comment = Comment.objects.get(id = comment_id)
            comment.delete()
            return HttpResponse('success')
        else:
            return HttpResponse('fail')
    else:
        return HttpResponse('fail')