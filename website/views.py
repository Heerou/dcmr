from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def home(request):
    #check if user is logged in
    if request.method == 'POST':
        usr = request.POST['username']
        passw = request.POST['password']
        #authenticate
        user =  authenticate(request, username=usr, password=passw)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been loggen in!")
            return redirect('home')
        else:
            messages.success(request, "Error in login the user...")
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authentice and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered a user')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})