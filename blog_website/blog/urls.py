from django.urls import path
from . import views  # Import views only from the `blog` app

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
]
