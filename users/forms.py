from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile
from django.utils import timezone
import datetime

class SignUpForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter Email')
    password1 = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)

    date_of_birth = forms.DateField(label='Date of Birth', input_formats=['%d/%m/%Y'])

    #Check if username alredy exists
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if len(username)>20:
            raise ValidationError('Username can not exceed 20 characters')
        if len(username)<3:
            raise ValidationError('Username must contain atleast 3 characters')
        if ' ' in username:
            raise ValidationError('Username must not contain any spaces')
        for ch in username:
            if not (ch.isalpha() or ch.isdigit() or ch == '.' or ch == '_'):
                raise ValidationError('Username must only contain alphabet, digits, \'.\' and \'_\' .')
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    #Check if email already exists
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    #Check if Passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    #Check if age is atleast 13 years
    def clean_date_of_birth(self):
        try:
            date_of_birth = self.cleaned_data['date_of_birth']
        except KeyError:
            raise ValidationError("Please enter Date of Birth.")
        if(timezone.now().date()-date_of_birth < datetime.timedelta(days=4748)):
            raise ValidationError("Age must be atleast 13 years to register")
        return date_of_birth

    #Check if name contains special characters
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name)<3 or len(first_name)>15:
            raise ValidationError("First name must contain between 3 and 15 letters")
        for ch in first_name:
            if not ch.isalpha() and ch!=' ':
                raise ValidationError("Name must not contain special characters or digits")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name)<3 or len(last_name)>15:
            raise ValidationError("Last name must contain between 3 and 15 letters")
        for ch in last_name:
            if not ch.isalpha() and ch!=' ':
                raise ValidationError("Name must not contain special characters or digits")
        return last_name

    #Save the form
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        new_profile = Profile(
            parent_user=user,
            date_of_birth=self.cleaned_data['date_of_birth'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        new_profile.save()
        return user


class EditProfileForm(forms.Form):
    userid = forms.CharField(widget=forms.HiddenInput())
    init_username = forms.CharField(widget=forms.HiddenInput())
    init_email = forms.EmailField(widget=forms.HiddenInput())

    username = forms.CharField(label='Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)

    date_of_birth = forms.DateField(label='Date of Birth', input_formats=['%d/%m/%Y'])

    def clean_userid(self):
        userid = self.cleaned_data['userid']
        return userid
    def clean_init_username(self):
        init_username = self.cleaned_data['init_username']
        return init_username
    def clean_init_email(self):
        init_email = self.cleaned_data['init_email']
        return init_email

    #Check if username alredy exists
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if username != self.cleaned_data['init_username']:
            if len(username)>20:
                raise ValidationError('Username can not exceed 20 characters')
            if len(username)<3:
                raise ValidationError('Username must contain atleast 3 characters')
            if ' ' in username:
                raise ValidationError('Username must not contain any spaces')
            for ch in username:
                if not (ch.isalpha() or ch.isdigit() or ch == '.' or ch == '_'):
                    raise ValidationError('Username must only contain alphabet, digits, \'.\' and \'_\' .')
                r = User.objects.filter(username=username)
            if r.count():
                raise  ValidationError("Username already exists")
        return username
    
    #Check if email already exists
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if email != self.cleaned_data['init_email']:
            r = User.objects.filter(email=email)
            if r.count():
                raise  ValidationError("Email already exists")
        return email

    #Check if age is atleast 13 years
    def clean_date_of_birth(self):
        try:
            date_of_birth = self.cleaned_data['date_of_birth']
        except KeyError:
            raise ValidationError("Please enter Date of Birth.")
        if(timezone.now().date()-date_of_birth < datetime.timedelta(days=4748)):
            raise ValidationError("Age must be atleast 13 years to register")
        return date_of_birth

    #Check if name contains special characters
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name)<3 or len(first_name)>15:
            raise ValidationError("First name must contain between 3 and 15 letters")
        for ch in first_name:
            if not ch.isalpha() and ch!=' ':
                raise ValidationError("Name must not contain special characters or digits")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if len(last_name)<3 or len(last_name)>15:
            raise ValidationError("Last name must contain between 3 and 15 letters")
        for ch in last_name:
            if not ch.isalpha() and ch!=' ':
                raise ValidationError("Name must not contain special characters or digits")
        return last_name
    
    #Save the form
    def save(self, commit=True):
        user = User.objects.get(pk = self.cleaned_data['userid'])
        profile = user.profile
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        profile.first_name = self.cleaned_data['first_name']
        profile.last_name = self.cleaned_data['last_name']
        profile.date_of_birth = self.cleaned_data['date_of_birth']
        user.save()
        profile.save()
        return user.username
