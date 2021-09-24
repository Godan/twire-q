from django.contrib import admin
from .models  import Question
from django.utils.html import mark_safe  # type: ignore
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "hashtag", "action_button"]
    
    def action_button(self, question: Question):
        if question.aggregate_start_time == None: 
            return mark_safe(f'<a class="button" href="">集計開始</a>')
        elif question.aggregate_start_time and not question.aggregate_end_time:
            return mark_safe(f'<a class="button" href="">集計終了</a>')


admin.site.register(Question, QuestionAdmin)
