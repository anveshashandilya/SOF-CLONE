from django.forms import ModelForm
from .models import *


class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=['title', 'detail']


class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=['detail']

class CommentQuestionForm(ModelForm):
    class Meta:
        model=CommentQuestion
        fields=['comment_question_text']

class CommentAnswerForm(ModelForm):
    class Meta:
        model=CommentAnswer
        fields=['detail']