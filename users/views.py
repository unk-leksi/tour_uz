# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from orders.models import Order

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to a home or dashboard page
        else:
            messages.error(request, 'There was an error with your registration.')
    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')  # Redirect to a home or dashboard page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'There was an error with your login.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard_view(request):
    orders = Order.objects.filter(user=request.user).select_related('excursion')
    return render(request, 'users/dashboard.html', {'orders': orders})