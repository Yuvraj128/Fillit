#127.0. 0.1 : 8000 127.0. 0.1 is the IP address of your local host 
# and 8000 is the default port on which it connects to Django webserver




from django.shortcuts import render, redirect
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def Indexpage(request):
    return render(request, 'index.html')



def user_register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            User.objects.create_user(username=username,email=email,password=password).save()
            messages.success(request,'The New User '+request.POST['username']+ ' is saved Successfully...!')
            return render(request, 'login.html')
        else:
            messages.warning(request, 'Password not matched with Confirm Password!')
            return render(request, 'signup.html')
        
    return render(request, 'signup.html')


def user_login(request):
     if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            login(request,user)
            #return HttpResponse('Logined Successfully  ' + request.POST['username'])
            return render(request,'index.html')
     return render(request, 'login.html')

def user_logout(request):
   logout(request)
   return HttpResponse('User Logged Out Successfully!!')
    



#def profiledata(request):
   # user_id = User.objects.get(id=id)
#    if request.method=='POST':
 #       FirstName=request.POST.get('FirstName')
  #      LastName=request.POST.get('LastName')
   #     Gender=request.POST.get('Gender')
    #    Address=request.POST.get('Address')
     #   user = User.objects.get(id=id)
   #     profile_obj =  Profile.objects.create(user=user, FirstName=FirstName, LastName=LastName, Gender=Gender, Address=Address)
    #    profile_obj.save()
     #   messages.success(request,'Your Profile data is saved Successfully...!')
        #view(request)
        #login_id = request.emails.id
       # return render(request,'myprofile.html')   
    #else:
     #   return render(request, 'profilepage.html')