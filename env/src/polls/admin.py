from django.contrib import admin
from .models import Questions, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'vote')
    list_filter = ['choice_text']
    search_fields = ['choice_text']

# Register your models herer.
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Choice, ChoiceAdmin)





