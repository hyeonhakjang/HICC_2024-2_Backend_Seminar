from django.urls import path

from . import views # .은 해당 폴더 (hiccproject) 의미

urlpatterns = [
	path('', views.index),
	# config 폴더의 path(‘home/’, include(‘hiccproject.urls’)), 코드와 합쳐서 	http://127.0.0.1:8000/home/ 경로가 됨

	path('question/', views.question, name = "question"),
	path('question/view/', views.question_view, name = "question_view"),
	path('question/create/', views.question_create, name = "question_create"),
	path('question/<int:question_id>/', views.question_detail, name = "question_detail"),
	path('question/<int:question_id>/view/', views.question_detail_view, name = "question_detail_view"),
	path('question/<int:question_id>/answer/view/', views.answer_view, name = "answer_view"),
	path('question/<int:question_id>/answer/create/', views.answer_create, name = "answer_create"),

]
