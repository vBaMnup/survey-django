from django.contrib import admin

from .models import Survey, Question, Option, Submission, Response, Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_filter = ("created_at",)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("survey", "prompt")
    list_filter = ("survey",)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("question", "text")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("survey", "created_at")
    list_filter = ("created_at",)


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("user", "survey", "question", "answer")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("submission", "option")
    list_filter = (
        "submission__survey",
        "option",
    )
