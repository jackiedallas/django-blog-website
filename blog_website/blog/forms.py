from django import forms  # type: ignore
from .models import Post, Comment, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        
        
class ProfileUpdateForm(forms.ModelForm):
    """Form to update user profile information including profile picture."""
    class Meta:
        model = Profile
        fields = ['profile_picture', 'bio']
