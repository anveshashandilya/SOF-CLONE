from django.contrib import admin

# Register your models here.
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display=('title', 'user')
    search_fields=('title', 'detail')


admin.site.register(Question, QuestionAdmin)
admin.site.register(CommentAnswer)
admin.site.register(CommentQuestion)
admin.site.register(Answer)
admin.site.register(UpVote)
admin.site.register(DownVote)
