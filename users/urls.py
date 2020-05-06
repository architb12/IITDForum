from django.urls import path

from . import views

app_name='users'
urlpatterns = [
    path('<str:u_name>/', views.profile_view, name='profile_view'),
    path('account/setup/', views.setup, name='setup'),
    path('account/setup2/', views.setup2, name='setup2'),
    path('account/setup3/', views.setup3, name='setup3'),
    path('account/setup4/', views.setup4, name='setup4'),
    path('account/edit/hostel/', views.edit_hostel, name='edit_hostel'),
    path('account/edit/dept/', views.edit_dept, name='edit_dept'),
    path('account/edit/bio/', views.edit_bio, name='edit_bio'),
    path('account/edit/profile/', views.edit_profile, name='edit_profile'),
    path('account/edit/image/', views.edit_image, name='edit_image'),
    path('account/delete/image/', views.delete_image, name='delete_image'),
    path('account/change_password/', views.change_password, name='change_password'),
    path('account/search/', views.search, name='search')
]