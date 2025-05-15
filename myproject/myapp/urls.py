from django.urls import path
from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('home/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    re_path(r'^search_food/$', views.search_food, name='search_food_query'),
]
