from django.shortcuts import render

from .models import Survey


def index(request):
    template = "survey/index.html"
    return render(request, template, {"title": "Сервис опросов!"})


def survey_list(request):
    surveys = Survey.objects.order_by("-created_at")
    return render(request, "survey/survey_list.html", {"surveys": surveys})


def survey_detail(request, pk):
    template = "survey/survey_detail.html"
    survey = Survey.objects.get(pk=pk)
    return render(request, template, {"name": survey.title})
