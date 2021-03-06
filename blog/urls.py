from django.urls import path
from . import views

urlpatterns = [
    path('home', views.post_list, name='post_list'),
    path('', views.welcome, name='welcome'),
    path('welcome', views.welcome, name='welcome'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
