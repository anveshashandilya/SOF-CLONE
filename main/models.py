from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Question Model
class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    detail=models.TextField()
    tags=models.TextField(default='')
    upvotes=models.IntegerField(default=0)
    downvotes=models.IntegerField(default=0)
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

# Answer Model
class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question_answer')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_answer')
    # parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    detail=models.TextField(null=False)
    upvotes=models.IntegerField(default=0)
    downvotes=models.IntegerField(default=0)
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

    # def get_responses(self):
    #     return Answer.objects.filter(parent=self)

#Comment on answer model
class CommentAnswer(models.Model):
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE)
    # question=models.ForeignKey(Question, on_delete=models.CASCADE,related_name='question_comment',blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='comment_answer_user')
    detail=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

#Comment on question model
class CommentQuestion(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='comment_question_user')
    comment_question_text=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_question_text

#Upvote on answer model
class UpVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='upvote_user')


#Downvote on answer model
class DownVote(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='downvote_user')

