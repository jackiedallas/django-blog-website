from django.contrib import admin # type: ignore
from .models import Post, Comment, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profile)
