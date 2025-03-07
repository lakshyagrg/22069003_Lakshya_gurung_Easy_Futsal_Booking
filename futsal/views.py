from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render (request,'home.html')

def login_view(request):
    if request.method =='POST':
        username=request.POST.get('Username')
        password=request.POST.get('password')
        user= authenticate(username=username,
                                password=password)
        
        if user is None:
            messages.info(request,'Username OR password is incorrect')
            return redirect('login')
        else:
            login(request,user)
            return redirect('home')
        
    return render(request,'login.html')

    
    
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        password1 = request.POST.get('Password1')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username is already taken.')
            return redirect('signup')


        if password != password1:
            messages.info(request, 'Passwords do not match.')
            return redirect('signup')

        # Create user
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully. Please log in.')
        return redirect('login')

    return render(request, 'signup.html')
    

def logout_view(request):
    logout(request)
    return redirect('home')
    
