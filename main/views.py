from django.shortcuts import render, HttpResponseRedirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, CommentQuestionForm, CommentAnswerForm
from .models import User
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, ListView, UpdateView, View

from django.contrib.auth import login,authenticate
from django.contrib.auth import login as site_login
from django.contrib.auth import logout as site_logout


#Login form
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('home'))
        #django login form will handle when the password etc is not valid automatically
    else:
        #In here, the method is GET as we're trying to get the empty form from the webpage
        #so that we could fill it
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Create your views here.
def home(request):
    questions=Question.objects.all().order_by('-id')

    question_form = QuestionForm(request.POST)
    if question_form.is_valid():
        question_form = question_form.save(commit=False)
        question_form.user = request.user
        question_form.save()
        return HttpResponseRedirect(reverse('home'))
    
        
    context = {
        'question_form':question_form,
    'questions':questions,
    # 'user': user
    }
    return render(request, 'home.html', context)






#Detail
def detail(request, id):
    question=Question.objects.get(pk=id)
    answers=Answer.objects.filter(question=question)


    
    answer_form = AnswerForm
    comment_question_form = CommentQuestionForm
    comment_answer_form = CommentAnswerForm


    if request.method == 'POST':
        # Answer form --- Add answer here
        if 'addanswer' in request.POST:
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.user = request.user
                answer.question = Question(id=id)
                answer.save()
                #kwargs id is used to redirect to the question detail page of that exact ques which 
                #we're on (same id)
                #notice how this wasn't needed in home index page bc we just display all questions
                return HttpResponseRedirect(reverse('detail', kwargs={'id':id}))

        # Comment for question Form
        elif 'questioncomment' in request.POST:
            comment_question_form = CommentQuestionForm(request.POST)
            if comment_question_form.is_valid():
                comment = comment_question_form.save(commit=False)
                comment.user = request.user
                comment.question = Question(id=id)
                comment.save()
                return HttpResponseRedirect(reverse('detail', kwargs={'id':id}))

        # Comment for answer Form
        elif 'answercomment' in request.POST:
            comment_answer_form = CommentAnswerForm(request.POST)
            if comment_answer_form.is_valid():
                # if request.POST.get('comment'):
                c_id=request.POST.get('answercomment')
                # p=request.POST.get('comment')
                comment = comment_answer_form.save(commit=False)
                comment.answer = Answer(id=c_id)
                comment.user = request.user 
                comment.save()
                return HttpResponseRedirect(reverse('detail',kwargs={'id':id}))
            # if comment_answer_form.is_valid():
            #     # question_id = request.POST.get('question')
            #     # parent_id = request.POST.get('parent')
            #     comment = comment_answer_form.save(commit=False)
            #     comment.user = request.user
            #     comment.question = Question(id=question_id)
            #     # comment.parent = Answer(id=parent_id)
            #     comment.save()
                
        

    return render(request, 'detail.html',{'question':question,
    'answers':answers, 'answer_form':answer_form, 
    'comment_question_form':comment_question_form,
    'comment_answer_form':comment_answer_form})
    
def upvote(request, id):
    if request.user.is_authenticated:
        if request.POST.get('like'):
              answer_id = request.POST['like']
              obj = Answer.objects.get(id=answer_id)
              obj.upvotes = obj.upvotes+1
              obj.save()
              return HttpResponseRedirect(reverse('detail',kwargs={'id':id}))
        obj = Question.objects.get(id=id)
        #remember: the id here is question id
        obj.upvotes = obj.upvotes+1
        obj.save()
        return HttpResponseRedirect(reverse('detail', kwargs = {'id':id}))


def downvote(request, id):
    if request.user.is_authenticated:
        if request.POST.get('dislike'):
            answer_id = request.POST['dislike']
            obj = Answer.objects.get(id=answer_id)
            obj.downvotes = obj.downvotes+1
            obj.save()
            return HttpResponseRedirect(reverse('detail',kwargs={'id':id}))
        obj = Question.objects.get(id=id)
        #remember: the id here is question id
        obj.downvotes = obj.downvotes+1
        obj.save()
        return HttpResponseRedirect(reverse('detail', kwargs = {'id':id}))

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    # messages.success(request,"Logged Out successfully")
    return redirect('/login/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return render(request,'profile.html',{'name':request.user})
        # return HttpResponseRedirect("/login/")
