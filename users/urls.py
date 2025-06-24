from django.urls import path
from .views import (
    ProfileDetailView
)
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", user_views.logout_view, name="logout"),
    path("profile/", user_views.profile, name="profile"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
