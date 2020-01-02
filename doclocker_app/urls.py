from django.urls import path
from . import views





urlpatterns = [
    path('', views.doclocker, name='doclocker'),
    path('homepage/', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.aboutus, name='aboutus'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    path('upload/', views.upload, name='upload'),





]