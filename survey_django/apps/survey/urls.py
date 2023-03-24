from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path("", views.index, name="index"),
    path("survey/", views.survey_list, name="survey_list"),
    path("survey/<int:pk>/", views.survey_detail, name="survey_detail"),
]
