from django.urls import path

from . import views # .은 해당 폴더 (hiccproject) 의미

app_name = 'hiccproject'

urlpatterns = [
	path('', views.index, name = "home"),
	# config 폴더의 path(‘home/’, include(‘hiccproject.urls’)), 코드와 합쳐서 	http://127.0.0.1:8000/home/ 경로가 됨

	path('question/', views.question, name = "question"),
	path('question/read/', views.question_read, name = "question_read"),
	path('question/create/', views.question_create, name = "question_create"),
	path('question/<int:question_id>/', views.question_detail, name = "question_detail"),
	path('question/<int:question_id>/read/', views.question_detail_read, name = "question_detail_read"),
	path('question/<int:question_id>/answer/read/', views.answer_read, name = "answer_read"),
	path('question/<int:question_id>/answer/create/', views.answer_create, name = "answer_create"),
	path('question/<int:question_id>/update/', views.question_update, name="question_update"),
	path('question/<int:question_id>/delete/', views.question_delete, name="question_delete"),
]
