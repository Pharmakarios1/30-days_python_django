from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'blog-home'),
    path('About', views.About, name= 'blog-About'),
    
]