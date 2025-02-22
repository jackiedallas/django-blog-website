from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import PostForm, CommentForm


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


def profile(request, username):
    """View to handle user profile and their posts."""
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-created_at')

    form = None  # Default to None for users who cannot post

    if request.user == user:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                # ✅ Fixed redirect
                return redirect('profile', username=request.user.username)
        else:
            form = PostForm()

    return render(request, 'blog/profile.html', {'user': user, 'posts': posts, 'form': form})


def post_detail(request, slug):
    """View to display a full blog post."""
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by('-created_at')
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)

    return render(request,
                  'blog/post_detail.html',
                  {
                      'post': post,
                      'comments': comments,
                      'form': form
                  }
                  )
