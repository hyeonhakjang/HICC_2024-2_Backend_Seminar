from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'hiccproject/index.html')

def question(request):
	return render(request, 'hiccproject/question.html')

def question_create(request):
	return render(request, 'hiccproject/question_create.html')