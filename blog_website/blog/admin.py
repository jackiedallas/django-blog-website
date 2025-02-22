from django.contrib import admin  # type: ignore
from .models import Post, Comment, Profile


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'approved')
    search_fields = ('author__username', 'post__title', 'body')


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile)
