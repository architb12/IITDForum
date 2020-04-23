from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib import messages
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
