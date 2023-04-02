from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.survey.urls", namespace="survey")),
    path("auth/", include("apps.user.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("accounts/", include("apps.user.urls")),
    path("admin/", admin.site.urls),
]
