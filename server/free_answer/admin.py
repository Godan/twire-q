from django.contrib import admin
from django.utils.html import mark_safe  # type: ignore
from django.urls import reverse_lazy

from .models  import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "hashtag", "action_button"]

    def action_button(self, question: Question):
        
        if question.aggregate_start_time == None: 
            url = reverse_lazy(
                "free_answer:start_aggregate", kwargs={"pk": question.pk}
            )
            return mark_safe(f'<a class="button" href="{url}">集計開始</a>')
        elif question.aggregate_start_time and not question.aggregate_end_time:
            url = reverse_lazy(
                "free_answer:end_aggregate", kwargs={"pk": question.pk}
            ) 
            return mark_safe(f'<a class="button" href="{url}">集計終了</a>')
        else:
            return mark_safe(f'<a class="button" href="">結果</a>')



admin.site.register(Question, QuestionAdmin)
