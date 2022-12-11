from django.urls import path

from . import views

urlpatterns = [
    path('',views.Indexpage, name='index'), 
    path('accounts/register', views.user_register, name='register'),
    path('accounts/Login', views.user_login, name='Login'),
    path('acccounts/Logout',views.user_logout,name = 'Logout'),
]
