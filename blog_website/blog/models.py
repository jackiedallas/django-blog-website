from django.db import models  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.utils.text import slugify  # type: ignore

# Post Model


class Post(models.Model):
    """Class representing a post being made to the blog site."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """Method to save the post."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """Method to return the post title."""
        return self.title

# Comment Model


class Comment(models.Model):
    """Class representing a comment on a blog post."""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    def __str__(self):
        """Return the comment on the blog post."""
        return f"Comment by {self.name} on {self.post.title}"

# Profile Model


class Profile(models.Model):
    """A class representing user profiles."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        """Return the user's username"""
        return f"{self.user.username}"
