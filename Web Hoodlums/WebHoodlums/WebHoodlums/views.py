from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from .models import UserProfile
# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmPassword']

        # Check if passwords match
        if password != confirm_password:
            return JsonResponse({'success': False, 'error': 'Passwords do not match'})

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'error': 'Username already exists'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Optionally, you can log in the user after signup
        auth.login(request, user)

        # Return a success response
        return JsonResponse({'success': True})

    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            # Access the has_signed_up attribute if applicable
            if hasattr(user, 'profile') and user.profile.has_signed_up:
                return JsonResponse({'success': True, 'signupCompleted': True})
            else:
                return JsonResponse({'success': True, 'signupCompleted': False})
        else:
            return JsonResponse({'success': False, 'error': 'Incorrect password or user does not exist'})
    else:
        return render(request, 'login.html')

def team(request):
    return render(request, 'OurTeam.html')

