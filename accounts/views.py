from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from taskApp import views


def signup(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['c-password']
        name = name.lower().replace(" ","")
        

        if password == confirm_password:

            if User.objects.filter(username=name).exists():
                print('error username')
                messages.error(request,'Name already exists')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('signup')
                else:
                    
                    user = User.objects.create(username=name,email=email,password=password)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Registeration Successful! Please try to login now.')
                    return redirect('login')
        else:
            messages.error(request,"Password doesn't match")
            print('error password')
            return redirect('signup')

    else:
        return render(request,'accounts/signup.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username =username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect(views.index)
            
            # return render(request,views.,{user:user})
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    
    auth_logout(request)
    messages.error(request,'You are logged out!')
    return redirect('login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')





















