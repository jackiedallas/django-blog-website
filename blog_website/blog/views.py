from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def landing_page(request):
    """View to handle the landing page."""
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to home page
    return render(request, 'blog/landing.html')


def register(request):
    """View to handle user registration."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log user in after registration
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html', {'form': form})


def home(request):
    """View to handle the home page."""
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

@login_required
def profile(request, username):
    """View to display and update user profile."""
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)  # ✅ Ensure profile exists
    posts = Post.objects.filter(author=user).order_by('-created_at')

    form = None  # ✅ Ensure form is always defined

    if request.user == user:
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)  # ✅ Handle image uploads
            if form.is_valid():
                form.save()
                return redirect('profile', username=user.username)  # ✅ Refresh profile page
        else:
            form = ProfileUpdateForm(instance=profile)  # ✅ Assign form even if no submission

    return render(request, 'blog/profile.html', {'user': user, 'profile': profile, 'posts': posts, 'form': form})

@login_required
def profile_settings(request):
    """View to allow users to update their profile."""
    profile, created = Profile.objects.get_or_create(user=request.user) # ensure profile exists
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'blog/profile_settings.html', {'form': form})


def post_detail(request, slug):
    """View to display a full blog post and its comments."""
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by('-created_at')  # ✅ Get approved comments
    form = CommentForm()

    if request.method == "POST":
        if request.user.is_authenticated:  # ✅ Ensure user is logged in before posting a comment
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user  # ✅ Assign the logged-in user as the author
                comment.save()
                return redirect('post_detail', slug=post.slug)  # ✅ Refresh page after submission
        else:
            return redirect('login')  # ✅ Redirect unauthenticated users to login before commenting

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})
