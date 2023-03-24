from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = "survey/index.html"
    return render(request, template, {"title": "Сервис опросов!"})


def survey_list(request):
    template = "survey/survey_list.html"
    return render(request, template, {"title": "Список всех опросов!"})


def survey_detail(request, pk):
    template = "survey/survey_detail.html"
    return render(request, template, {"title": f"Опрос {pk}"})
