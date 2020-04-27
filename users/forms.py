from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile
from django.utils import timezone
import datetime

class SignUpForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)

    years_list=[year for year in range(1950,timezone.now().year)]
    date_of_birth = forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=years_list),initial="2000-01-01")

    gender_choices = ( 
        ("Male", "Male"), 
        ("Female", "Female"), 
        ("Other", "Other"), 
    ) 
    gender = forms.ChoiceField(label='Gender',choices=gender_choices)


    #Check if username alredy exists
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
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
        date_of_birth = self.cleaned_data['date_of_birth']
        if(timezone.now().date()-date_of_birth < datetime.timedelta(days=4748)):
            raise ValidationError("Age must be atleast 13 years to register")
        return date_of_birth

    #Check if name contains special characters
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        for ch in first_name:
            if not ch.isalpha() and ch!=' ':
                raise ValidationError("Name must not contain special characters or digits")
        return first_name

    def clean_second_name(self):
        second_name = self.cleaned_data['second_name']
        for ch in second_name:
            if not ch.isalpha() and ch!=' ':
                raise ValidationError("Name must not contain special characters or digits")
        return second_name

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
            gender=self.cleaned_data['gender'],
        )
        new_profile.save()
        return user
