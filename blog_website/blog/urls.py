from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('create-post/', views.create_post, name='create_post'),
    path("post/edit/<int:post_id>/", views.edit_post, name="edit_post"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Add this for post details
]
