from django.urls import path

from . import views

app_name='users'
urlpatterns = [
    path('<str:u_name>/', views.profile_view, name='profile_view'),
]