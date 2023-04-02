from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from apps.user.forms import RegisterForm, ProfileEditForm


def register(request):
    if request.method == "GET":
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect("survey:index")
    return render(request, "user/register.html", {"form": form})


def profile(request):
    user = request.user
    email = user.email
    first_name = user.first_name
    last_name = user.last_name
    score = user.score
    context = {
        "user": user,
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "score": score,
    }
    return render(request, "user/profile.html", context)


def profile_edit(request):
    user = request.user
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен.")
            return redirect("profile")
    else:
        form = ProfileEditForm(instance=user)
    context = {
        "form": form,
    }
    return render(request, "user/profile_edit.html", context)
