from django.urls import path

from . import views # .은 해당 폴더 (hiccproject) 의미

urlpatterns = [
	path('', views.index),
	path('question/', views.question),
	path('question/create/', views.question_create),
	# config 폴더의 path(‘home/’, include(‘hiccproject.urls’)), 코드와 합쳐서 	http://127.0.0.1:8000/home/ 경로가 됨
]
