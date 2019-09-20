from django.shortcuts import render, redirect
from .models import Question, Answer

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pk')
    context = {'questions': questions,}
    return render(request, 'eithers/index.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        issue_a = request.POST.get('issue_a')
        issue_b = request.POST.get('issue_b')
        image_a = request.FILES.get('image_a')
        image_b = request.FILES.get('image_b')
        question = Question(title=title, issue_a=issue_a, issue_b=issue_b, image_a=image_a, image_b=image_b)
        question.save()
        return redirect('question:index')
    else:
        return render(request, 'eithers/new.html')

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    answers = question.answer_set.all()
    count = 0
    count_1 = 0
    percent = 0
    percent_1 = 0
    for answer in answers:
        count += 1
        if answer.pick:
            count_1 += 1
    if count:
        percent = ((count - count_1) / count) * 100
        percent_1 = count_1 * 100 / count
    context = {'question': question, 'answers': answers, 'percent': percent, 'percent_1': percent_1}
    return render(request, 'eithers/detail.html', context)

def answers_create(request, question_pk):    
    if request.method == 'POST':
        question = Question.objects.get(pk=question_pk)
        content = request.POST.get('answer')
        pick = request.POST.get('pick')
        comment = Answer(question=question, pick=pick, comment=content)
        comment.save()
        return redirect('question:detail', question_pk)
    else:
        return redirect('question:detail', question_pk)

def answers_delete(request, question_pk, answer_pk):
    if request.method == 'POST':
        comment = Answer.objects.get(pk=answer_pk)
        comment.delete()
    return redirect('question:detail', question_pk)