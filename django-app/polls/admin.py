from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Choice Information', {'fields': ['choice_text', 'votes']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
