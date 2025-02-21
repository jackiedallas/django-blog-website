from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth import login  # type: ignore
from django.contrib.auth.forms import UserCreationForm  # type: ignore

# Create your views here.

# Landing Page


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # redirect logged in users to home page
    return render(request, 'blog/landing.html')

# registration page


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in after registration
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def home(request):  # This function must exist!
    return render(request, 'blog/home.html')
