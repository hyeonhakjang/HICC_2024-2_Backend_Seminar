from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.http import JsonResponse
from hiccproject.models import *
# Create your views here.

def index(request):
	return render(request, 'hiccproject/index.html')

def question(request):
	return render(request, 'hiccproject/question.html')

def question_create(request):
	if request.method == 'POST':
		question = Question(subject = request.POST.get('subject'), content = request.POST.get('content'), create_date=timezone.now())
		question.save()
		return redirect('question')
	else:
		return render(request, 'hiccproject/question_create.html')

def question_read(request):
	questions = Question.objects.all().values('id', 'subject', 'content', 'create_date')

	return JsonResponse({'questions' : list(questions)}) # json 형식으로 설정 후 response

def question_detail(request, question_id):
	question = get_object_or_404(Question, id = question_id) #question_id가 존재하지 않는 페이지로 들어가면 404 에러가 뜨도록 설정
	return render(request, 'hiccproject/question_detail.html')

def question_detail_read(request, question_id):
	question = Question.objects.get(id = question_id)

	question_data = {
		'id': question.id,
		'subject': question.subject,
		'content': question.content,
		'create_date': question.create_date
	}

	return JsonResponse(question_data)


def answer_read(request, question_id):
	question = Question.objects.get(id = question_id)

	answers = Answer.objects.filter(question = question_id).values('id', 'question_id', 'content', 'create_date')

	return JsonResponse({'answers' : list(answers)})

def answer_create(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    answer = Answer(question=question, content=request.POST.get('answer_content'), create_date=timezone.now())
    answer.save()
    return redirect('question_detail', question_id=question.id)

def question_update(request, question_id):
	if request.method == 'POST':
		question = Question(id = question_id, subject = request.POST.get('subject'), content = request.POST.get('content'), create_date=timezone.now())
		question.save()
		return redirect('question')
	else:
		return render(request, 'hiccproject/question_update.html')

def question_delete(request, question_id):
	question = get_object_or_404(Question, id = question_id)
	question.delete()
	return redirect('question')