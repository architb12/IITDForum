from django.contrib.auth.forms import UserCreationForm
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

    years_list=[year for year in range(1950,timezone.now().year)]
    date_of_birth = forms.DateField(label='Date of Birth', input_formats=['%d/%m/%Y'])

    gender_choices = ( 
        ("Male", "Male"), 
        ("Female", "Female"), 
        ("Other", "Other"), 
    )
    gender = forms.ChoiceField(label='Gender',choices=gender_choices)

    dept_choices = (
        ("None", "None"),
        ("Biochemical Engineering and Biotechnology", "Biochemical Engineering and Biotechnology"), 
        ("Chemical Engineering", "Chemical Engineering"),
        ("Civil Engineering", "Civil Engineering"),
        ("Computer Science", "Computer Science"),
        ("Electrical Engineering", "Electrical Engineering"),
        ("Physics", "Physics"),
        ("Mathematics", "Mathematics"),
        ("Mechanical Engineering", "Mechanical Engineering"),
        ("Textile Technology", "Textile Technology"),
    )
    dept = forms.ChoiceField(label='Department',choices=dept_choices)

    hostel_choices = (
        ("None", "None"),
        ("Aravali", "Aravali"), 
        ("Girnar", "Girnar"),
        ("Himadri", "Himadri"),
        ("Jwalamukhi", "Jwalamukhi"),
        ("Kailash", "Kailash"),
        ("Karakoram", "Karakoram"),
        ("Kumaon", "Kumaon"),
        ("Nilgriri", "Nilgriri"),
        ("Satpura", "Satpura"),
        ("Shivalik", "Shivalik"),
        ("Udaigiri", "Udaigiri"),
        ("Vindhyachal", "Vindhyachal"),
        ("Zanskar", "Zanskar"),
    )
    hostel = forms.ChoiceField(label='Hostel',choices=hostel_choices)

    #Check if username alredy exists
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if len(username)>30:
            raise ValidationError('Username can not exceed 30 characters')
        if len(username)<3:
            raise ValidationError('Username must contain atleast 3 characters')
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
            gender=self.cleaned_data['gender'],
            dept=self.cleaned_data['dept'],
            hostel=self.cleaned_data['hostel'],
        )
        new_profile.save()
        return user
