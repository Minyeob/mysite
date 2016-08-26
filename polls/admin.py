from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 ('Question Statement', {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date', 'mod_date']}),
                 
                ]
    inlines = [ChoiceInline]            
    list_display = ('question_text', 'pub_date', 'mod_date')
    list_filter = ['mod_date']
    search_fields = ['question_text']
                


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

