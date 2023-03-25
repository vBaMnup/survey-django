from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Survey(models.Model):
    """Опросы созданные пользователем"""

    title = models.CharField("Название опроса", max_length=128)
    description = models.TextField("Описание", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    award = models.IntegerField("Награда")
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Вопросы для опросов"""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    prompt = models.CharField("Подсказка", max_length=255)

    def __str__(self):
        return f"{self.survey}: {self.prompt}"


class Option(models.Model):
    """Варианты с несколькими вариантами ответа."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Submission(models.Model):
    """набор ответов для вопросов"""

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.survey}: {self.created_at}"


class Answer(models.Model):
    """Ответ на вопросы"""

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)


class Response(models.Model):
    """Модель для связи пользователя и опросов"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="completed_surveys"
    )
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    answered_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}: {self.survey}"
