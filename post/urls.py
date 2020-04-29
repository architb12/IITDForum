from django.urls import path
from . import views

app_name='post'
urlpatterns = [
    path('<int:post_id>/', views.post_view, name='post_view'),
    path('like/', views.post_like, name='post_like'),
    path('createpost/', views.post_create, name='post_create'),
    path('deletepost/', views.post_delete, name='post_delete'),
    path('deletecomment/', views.comment_delete, name='comment_delete')
]