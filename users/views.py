from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import Http404
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
            return redirect('users:setup')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form':form})

def profile_view(request, u_name):
    try:
        user = User.objects.get(username=u_name)
    except User.DoesNotExist:
        raise Http404("ERROR 404: User does not exist")
    posts = user.post_set.all().order_by('-pub_date')
    return render(request, 'users/profile.html', {'user': user, 'posts':posts, 'title': user.username})

def setup(request):
    if request.user.is_authenticated:
        return render(request,'users/setup.html')
    else:
        return redirect('home')

def setup2(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            dept = request.POST['dept']
            if(dept!='Skip'):
                profile = request.user.profile
                profile.dept = dept
                profile.save()
            return render(request,'users/setup2.html')     
        else:
            return redirect('home')
    else:
        return redirect('home')

def setup3(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            hostel = request.POST['hostel']
            if(hostel!='Skip'):
                profile = request.user.profile
                profile.hostel = hostel
                profile.save()
            messages.success(request, f'Your profile has been set up successfully!')
            return redirect('users:profile_view', u_name=request.user.username)     
        else:
            return redirect('home')
    else:
        return redirect('home')
