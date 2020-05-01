from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.http import HttpResponse
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
            messages.success(request, f'Authorized')
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
        storage = messages.get_messages(request)
        for message in storage:
                if message.message=='Authorized':
                    del storage._loaded_messages[-1]
                    return render(request,'users/setup.html',{'title': 'Select your Department'})
        return redirect('home')
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
            return render(request,'users/setup2.html',{'title': 'Select your Hostel'})     
        else:
            return redirect('home')
    else:
        return redirect('home')

def setup3(request):
    if request.user.is_authenticated:
        storage = messages.get_messages(request)
        for message in storage:
                if message.message=='Bio exceeds character limit.':
                    storage.used = False
                    return render(request,'users/setup3.html',{'title': 'Write a bio'}) 
        storage.used = False
    if request.method=='POST':
        if request.user.is_authenticated:
            hostel = request.POST['hostel']
            if(hostel!='Skip'):
                profile = request.user.profile
                profile.hostel = hostel
                profile.save()
            return render(request,'users/setup3.html',{'title': 'Write a bio'})   
        else:
            return redirect('home')
    else:
        return redirect('home')

def setup4(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            try:
                skip = request.POST['skip-btn']
                messages.success(request,f'Your profile has been set up successfully!')
                return redirect('users:profile_view', u_name=request.user.username)
            except KeyError:
                bio = request.POST['bio-text']
                if len(bio)>200:
                    messages.warning(request, f'Bio exceeds character limit.')
                    return redirect('users:setup3')
                profile = request.user.profile
                profile.bio = bio
                profile.save()
                messages.success(request,f'Your profile has been set up successfully!')
                return redirect('users:profile_view', u_name=request.user.username)
        else:
            return redirect('home')
    else:
        return redirect('home')

#Edit Hostel view
def edit_hostel(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            hostel = request.POST['hostel']
            if(hostel!='Skip'):
                profile = request.user.profile
                profile.hostel = hostel
                profile.save()
                messages.success(request, f'Hostel updated')
            return redirect('users:profile_view', u_name=request.user.username)
        else:
            return render(request,'users/edit_hostel.html',{'title': 'Change your hostel'})
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')

#Edit Department view
def edit_dept(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            dept = request.POST['dept']
            if(dept!='Skip'):
                profile = request.user.profile
                profile.dept = dept
                profile.save()
                messages.success(request, f'Department updated')
            return redirect('users:profile_view', u_name=request.user.username)
        else:
            return render(request,'users/edit_dept.html',{'title': 'Change your department'})
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')

#Edit Bio view
def edit_bio(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            try:
                skip = request.POST['skip-btn']
                return redirect('users:profile_view', u_name=request.user.username)
            except KeyError:
                bio = request.POST['bio-text']
                if len(bio)>200:
                    messages.warning(request, f'Bio exceeds character limit.')
                    return redirect('users:edit_bio')
                profile = request.user.profile
                profile.bio = bio
                profile.save()
                messages.success(request,f'Bio updated')
                return redirect('users:profile_view', u_name=request.user.username)
        else:
            return render(request,'users/edit_bio.html',{'title': 'Edit your bio'})
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')