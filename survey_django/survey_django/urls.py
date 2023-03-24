from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.survey.urls", namespace="survey")),
    path("admin/", admin.site.urls),
]
