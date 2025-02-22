from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/settings/', views.profile_settings, name='profile_settings'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),  # Add this for post details
]
