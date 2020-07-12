from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_info,name="index"),
    path('forms/',views.forms,name="forms"),
    path('home/',views.home,name="home"),
    path('article/',views.article,name="article"),
    path('forms/main/',views.main,name="main"),
    path('main/',views.main,name="main"),
    path('article/main/',views.main,name="main"),
    path('home/main/',views.main,name="main"),
]
