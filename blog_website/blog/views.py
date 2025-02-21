from django.shortcuts import render, redirect

# Create your views here.

# Landing Page
def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home') # redirect logged in users to home page
    return render(request, 'blog/landing.html')

