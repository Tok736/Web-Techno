from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *

# Create your views here.

class Questions_List(View):
    def get(self, request):
        n_question_on_page = 3
        questions = Question.objects.all()
        paginator = Paginator(questions, n_question_on_page)
        page = request.GET.get('page')
        try:
            questions = paginator.page(page)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)
        return render(request, 'cat_questions/questions_list.html', context={
            "questions": questions,
        })

    # def post(self, request):


class Questions_List_Hot(View):
    def get(self, request):
        questions = Question.objects.hot()
        return render(request, 'cat_questions/questions_list.html', context={
            "questions": questions,
        })

class Questions_List_Newest(View):
    def get(self, request):
        questions = Question.objects.newest()
        return render(request, 'cat_questions/questions_list.html', context={
            "questions": questions,
        })

class Question_Details(View):
    def get(self, request, id):
        question = get_object_or_404(Question, id=id)
        answers = question.answers.all().exclude(is_right = True)
        right_answer = question.answers.get(is_right = True)
        return render(request, 'cat_questions/question_details.html', context={
            "question": question,
            "answers": answers,
            "right_answer": right_answer
        })


class Tags_List(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, 'cat_questions/tags_list.html', context={
            'tags': tags,
        })


class Tag_Details(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        return render(request, 'cat_questions/tag_details.html', context={
            'tag': tag,
        })


class Register(View):
    def get(self, request):
        return render(request, 'cat_questions/register.html')


class Sign_In(View):
    def get(self, request):
        return render(request, 'cat_questions/sign_in.html')

class Ask_Page(View):
    def get(self, request):
        form = AskForm()
        return render(request, 'cat_questions/ask.html', context={
            'form': form
        })

    def post(self, request):
        pass

class Profile_Settings(View):
    def get(self, request):
        return render(request, 'cat_questions/profile_settings.html')



