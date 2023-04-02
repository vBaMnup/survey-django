from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.user import views as user_views

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    # выход из системы
    path(
        "logout/",
        login_required(auth_views.LogoutView.as_view(template_name="user/logout.html")),
        name="logout",
    ),
    path("profile/", login_required(user_views.profile), name="profile"),
    path("profile/edit/", login_required(user_views.profile_edit), name="profile_edit"),
]
