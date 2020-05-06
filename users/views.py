from django.shortcuts import render,redirect
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.http import Http404
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
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

#Edit Profile View
def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = request.POST.copy()
            post['userid'] = request.user.id
            post['init_username'] = request.user.username
            post['init_email'] = request.user.email
            form = EditProfileForm(post)
            if form.is_valid():
                new_username = form.save()
                messages.success(request, f'Profile updated successfully!')
                return redirect('users:profile_view', u_name=new_username)
            else:
                return render(request, 'users/edit_profile.html', {'form':form, 'title': 'Edit your profile'})
        else:
            form = EditProfileForm(initial = {
                'userid': request.user.id,
                'username': request.user.username,
                'init_username': request.user.username,
                'email': request.user.email,
                'init_email': request.user.email, 
                'first_name': request.user.profile.first_name,
                'last_name': request.user.profile.last_name,
                'date_of_birth': request.user.profile.date_of_birth,
            })
            return render(request, 'users/edit_profile.html', {'form':form, 'title': 'Edit your profile'})
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')

#Search User View
def search(request):
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
            html += '<li><a href="'
            html += '/users/' + user.username +'/"'
            html +=  'class="liker-link"> ' 
            html += '<div class="row user-wrapper"> <div class="col-md-3"> <img class="img-circle profile-pic" width=40 height=40 src="'
            html += user.profile.image.url
            html += '" alt="default.jpg"> </div> <div class="col-md-9"> '
            html += ' <font class="liker-username-font"> '
            html += user.username
            html += ' </font> <br> <font class="liker-name-font"> '
            html += user.profile.full_name()
            html += ' </font> </div> </div> </a> </li> '

        return HttpResponse(html)
    else:
        return HttpResponse('fail')


#Edit Image View
def edit_image(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            profile = user.profile
            try:
                img = request.FILES['image_input']
                try:
                    image = Image.open(img)
                    w,h = image.size
                    if w > h:
                        top = 0
                        bottom = h
                        left = (w-h)/2
                        right = (w+h)/2
                    else:
                        top = (h+w)/2
                        bottom = (h-w)/2
                        left = 0
                        right = w
                    img_io = BytesIO()
                    cropped_image = image.crop((left, top, right, bottom))
                    resized_image = cropped_image.resize((300, 300), Image.ANTIALIAS)
                    resized_image.save(img_io, format='JPEG', quality=100)
                    img_content = ContentFile(img_io.getvalue(), str(user.id)+'_image.jpg')
                    if user.profile.image.url == "/media/default.jpg":
                        profile.image = img_content
                        profile.save()
                    else:
                        profile.image.delete()
                        profile.image = img_content
                        profile.save()
                    return redirect('users:profile_view', u_name=user.username)
                except:
                    messages.warning(request, f'File format is not supported')
                    return redirect('users:profile_view', u_name=user.username)
            except:
                messages.warning(request, f'Please choose a picture to upload.')
                return redirect('users:profile_view', u_name=user.username)
        else:
            return redirect('users:profile_view', u_name=user.username)
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')

#Delete image view
def delete_image(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            profile = user.profile
            if user.profile.image.url == "/media/default.jpg":
                messages.warning(request, f'You don\'t have a profile picture yet.')
                return redirect('users:profile_view', u_name=user.username)
            else:
                profile.image.delete()
                profile.image = 'default.jpg'
                profile.save()
                messages.success(request, 'Profile picture deleted.')
                return redirect('users:profile_view', u_name=user.username)
        else:
            return redirect('users:profile_view', u_name=user.username)
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')

#Change Password View
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, f'Your password has been changed.')
                return redirect('users:profile_view', u_name=user.username)
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'users/change_password.html', {'form': form})
    else:
        messages.warning(request, f'Please login or create an account.')
        return redirect('home')
