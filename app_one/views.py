from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='signin')
def home(request):
    return render(request, 'app_one/accounts/home.html')

def signin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        this_user = authenticate(request, email=email, password=password)

        if this_user is not None:
            login(request, this_user)
            messages.success(request, 'You have successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('signin')

    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('home')

    return render(request, 'app_one/accounts/signin.html')


def signup(request):

    if request.method == 'POST':
        email = request.POST['email']

        if not email.endswith('@staff.mak.ac.g'):
            messages.error(request, 'Only staff emails are allowed')
            return redirect('signup')
            
        username = request.POST['username']
        first_name = request.POST['first_name']
        surname = request.POST['surname']
        middle_name = request.POST['middle_name']
        department = request.POST['department']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
        else:
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')
            elif CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            else:
                new_user = CustomUser.objects.create_user(email=email, username=username, password=password1)
                new_user.first_name = first_name
                new_user.surname = surname
                new_user.middle_name = middle_name
                # new_user.department = department
                new_user.save()
                messages.success(request, 'You have successfully created an account')
                return redirect('signin')

    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in')
        return redirect('home')

    return render(request, 'app_one/accounts/signup.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('signin')
