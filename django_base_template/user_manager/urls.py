from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.custom_login, name="login"),
    path("logout", views.custom_logout, name="logout"),
    path("profile/<username>", views.profile, name="profile"),
    path(
        "profile_settings/<username>", views.profile_settings, name="profile_settings"
    ),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path(
        "reset/<uidb64>/<token>",
        views.passwordResetConfirm,
        name="password_reset_confirm",
    ),
]
