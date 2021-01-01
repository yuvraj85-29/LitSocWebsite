from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
path('',views.home,name='blog-home'),
path('about/',views.about,name='blog-about'),
path('new/',views.new,name='blog-new'),
path('p1/',views.p1,name='blog-p1'),
path('p2/',views.p2,name='blog-p2'),
path('p3/',views.p3,name='blog-p3'),
path('p4/',views.p4,name='blog-p4'),
path('p5/',views.p5,name='blog-p5'),
]
