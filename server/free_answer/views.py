from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse, HttpResponse

from free_answer.models import Question
# Create your views here.

class StartAggregate(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, pk, *args, **kwargs):
        question: Question = Question.objects.get(pk=pk)
        question.start_aggreagate()
        return JsonResponse({"status": "success"})
