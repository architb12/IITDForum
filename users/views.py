from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
# Create your views here.

# View For sign up form
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created for {username}!')
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form':form})

def profile_view(request, u_name):
    try:
        user = User.objects.get(username=u_name)
    except User.DoesNotExist:
        raise Http404("ERROR 404: User does not exist")
    posts = user.post_set.all().order_by('-pub_date')
    return render(request, 'users/profile.html', {'user': user, 'posts':posts, 'title': user.username})
