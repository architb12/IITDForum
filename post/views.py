from django.shortcuts import render, redirect
from .models import Post, Comment, PostLike, Tag
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
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
    return render(request,'post/home.html',{'posts':posts, 'title':'Home'})

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

                #Utility function to identify tags from text
                tag_list = []
                tokens = post_text.split(' ')
                for token in tokens:
                    try:
                        if token[0]=='@' and len(token)>3 and len(token)<22:
                            valid = True
                            for ch in token[1:]:
                                if ch!='.' and ch!='_' and not ch.isalpha() and not ch.isdigit():
                                    valid = False
                                    break
                            if valid:
                                try:
                                    tagged_user = User.objects.get(username=token[1:])
                                    if request.user != tagged_user and not tagged_user in tag_list:
                                        tag_list.append(tagged_user)
                                except: 
                                    continue
                    except:
                        continue
                
                #Checks if user already has atleast 10 tags and removes oldest tag if required
                #Takes only the first 10 tags from the post
                for tagged_user in tag_list[:10]:
                    if tagged_user.tag_set.count() >= 10:
                        remove_tag = tagged_user.tag_set.order_by('pub_date')[0]
                        remove_tag.delete()
                    new_tag = Tag(parent_user=tagged_user,tagger_id=str(request.user.id),tag_type='post',pub_date=timezone.now(),post_id=new_post.id)
                    new_tag.save()
                    

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

                #Utility function to identify tags from text
                tag_list = []
                tokens = comment_text.split(' ')
                for token in tokens:
                    try:
                        if token[0]=='@' and len(token)>3 and len(token)<22:
                            valid = True
                            for ch in token[1:]:
                                if ch!='.' and ch!='_' and not ch.isalpha() and not ch.isdigit():
                                    valid = False
                                    break
                            if valid:
                                try:
                                    tagged_user = User.objects.get(username=token[1:])
                                    if request.user != tagged_user and not tagged_user in tag_list and post.author != tagged_user:
                                        tag_list.append(tagged_user)
                                except: 
                                    continue
                    except:
                        continue
                
                #Checks if user already has atleast 10 tags and removes oldest tag if required 
                #Takes only the first 10 tags from the comment
                for tagged_user in tag_list[:10]:
                    if tagged_user.tag_set.count() >= 10:
                        remove_tag = tagged_user.tag_set.order_by('pub_date')[0]
                        remove_tag.delete()
                    new_tag = Tag(
                        parent_user=tagged_user,
                        tagger_id=str(request.user.id),
                        tag_type='comment',
                        pub_date=timezone.now(),
                        post_id=new_comment.parent_post.id
                        )
                    new_tag.save()
                
                #For creating 'commented' tag for notifications
                if post.author != new_comment.author:
                    if post.author.tag_set.count() >= 10:
                            remove_tag = tagged_user.tag_set.order_by('pub_date')[0]
                            remove_tag.delete()
                    new_tag = Tag(
                        parent_user=post.author,
                        tagger_id=str(request.user.id),
                        tag_type='commented',
                        pub_date=timezone.now(),
                        post_id=new_comment.parent_post.id
                        )
                    new_tag.save()

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
            return HttpResponse('success',)
        else:
            return HttpResponse('fail')
    else:
        return HttpResponse('fail')

#Post tag suggestions
def tag_search(request):
    if request.method == 'GET':
        search_text = request.GET['search_text'].lower()
        users = User.objects.all()
        valid_users = []
        def check_valid(user):
            if user.username.lower().find(search_text) != -1:
                return True
            if user.profile.first_name.lower().find(search_text) != -1:
                return True
            if user.profile.last_name.lower().find(search_text) != -1:
                return True
            return False
            
        for user in users:
            if check_valid(user):
                valid_users.append(user)
            if len(valid_users)>4:
                break
        
        html = ""
        for user in valid_users:
            html += '<div class="tag-suggestion" onclick="tag_complete(this.id)"; id="'
            html += user.username + '"> ' 
            html += '<div class="row user-wrapper"> <div class="col-md-3"> <img class="img-circle profile-pic" width=40 height=40 src="'
            html += user.profile.image.url
            html += '" alt="default.jpg"> </div> <div class="col-md-9"> '
            html += ' <font class="liker-username-font"> '
            html += user.username
            html += ' </font> <br> <font class="liker-name-font"> '
            html += user.profile.full_name()
            html += ' </font> </div> </div> </div> '

        return HttpResponse(html)
    else:
        return HttpResponse('fail')

def tag_view(request,tag_id):
    if request.user.is_authenticated:
        tag = Tag.objects.get(id=tag_id)
        if request.user == tag.parent_user:
            user = tag.parent_user
            seen_tags = Tag.objects.filter(parent_user=user,post_id=tag.post_id)
            for seen_tag in seen_tags:
                seen_tag.seen = True
                seen_tag.save()
            return redirect('post:post_view',post_id=tag.post_id)
        else:
            return redirect('home')
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')
    

def mark_as_read(request):
    if request.user.is_authenticated:
        tags = request.user.tag_set.filter(seen=False)
        for tag in tags:
            tag.seen = True
            tag.save()
        return redirect('home')
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')