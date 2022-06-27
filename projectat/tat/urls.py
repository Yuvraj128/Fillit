import imp
from django.urls import path
from . import views


urlpatterns = [
    path('',views.indexe,name='index'),
    path('cont',views.cont,name='cont'),
    path('abt',views.abt,name='abt'),
    path('destinations',views.destinations,name='destinations'),
    path('user_login1',views.user_login1,name='login1'),
    path('covid',views.covid,name='covid'),
    
    path('user_login',views.user_login,name='login2'),
    path('register',views.register,name='register'),
]   