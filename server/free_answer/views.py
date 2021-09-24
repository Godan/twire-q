from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from free_answer.models import Question
from free_answer.application import FreeAnswerApplication
# Create your views here.

class StartAggregate(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, pk, *args, **kwargs):
        question: Question = Question.objects.get(pk=pk)
        application: FreeAnswerApplication = FreeAnswerApplication()

        application.start_aggregate(question)
        return redirect(reverse("admin:free_answer_question_changelist"))