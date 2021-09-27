from django.shortcuts import render
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
 
from free_answer.models import Question
from free_answer.application import FreeAnswerApplication
from infrastructures.twitter.adapter import TwitterAdapter

class StartAggregate(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, pk, *args, **kwargs):
        question: Question = Question.objects.get(pk=pk)
        application: FreeAnswerApplication = FreeAnswerApplication()

        application.start_aggregate(question)
        adapter = TwitterAdapter()
        return redirect(reverse("admin:free_answer_question_changelist"))


class EndAggregate(LoginRequiredMixin, View):
    def get(self, request: HttpRequest, pk, *args, **kwargs):
        question: Question = Question.objects.get(pk=pk)
        application: FreeAnswerApplication = FreeAnswerApplication()

        application.end_aggregate(question)
        tweets = application.search_tweets_from_question(question)
        application.save_tweets(question, tweets)

        return redirect(reverse("admin:free_answer_question_changelist"))

class AnswerView(DetailView):
    template_name = 'free_answer/answer.html'
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import json
        context['tweets'] = json.loads(context["object"].result_json)
        print(context['tweets'])

        return context
