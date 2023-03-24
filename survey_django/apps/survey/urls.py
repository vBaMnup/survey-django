from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("survey/", views.survey_list),
    path("survey/<int:pk>/", views.survey_detail),
]
