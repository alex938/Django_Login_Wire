from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, logout, login as login_auth
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')
        if all([name, email, password, password_confirm]):
            if password == password_confirm:
                try:
                    new_user = User.objects.create_user(name=name, email=email, password=password)
                    new_user.save()
                    return redirect('account:login') 
                except Exception as e:
                    messages.error(request, f"Error: {str(e)}")
            else:
                messages.error(request, "Passwords do not match.")
        else:
            messages.error(request, "Please fill out all fields.")
        return render(request, 'account/signup.html')
    else:
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if all([email and password]):
            user = authenticate(request, email=email, password=password, backend='account.User')
            if user is not None:
                login_auth(request, user)
                return redirect('/')
        else:
                print('Invalid email or password')
                return render(request, 'account/login.html', {'error': 'Invalid email or password'})
    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('core:homepage') 