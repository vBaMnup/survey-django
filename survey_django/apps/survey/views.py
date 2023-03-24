from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница")


def survey_list(request):
    return HttpResponse("Список опросов")


def survey_detail(request, pk):
    return HttpResponse(f"Опрос номер {pk}")
