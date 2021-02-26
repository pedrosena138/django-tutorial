from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text', 'votes']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
