from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import RedirectView
# Create your views here.

#View individual post with comments
def post_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("ERROR 404: Post does not exist")
    comments = post.comment_set.order_by('-pub_date')
    return render(request, 'post/post_view.html', {'post': post, 'comments': comments})

#Home page 
def home(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request,'post/home.html',{'posts':posts})

class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        id=self.kwargs.get("id")
        

