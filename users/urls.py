from django.urls import path

from . import views

app_name='users'
urlpatterns = [
    path('<str:u_name>/', views.profile_view, name='profile_view'),
    path('account/setup/', views.setup, name='setup'),
    path('account/setup2/', views.setup2, name='setup2'),
    path('account/setup3/', views.setup3, name='setup3'),
    path('account/setup4/', views.setup4, name='setup4'),
]