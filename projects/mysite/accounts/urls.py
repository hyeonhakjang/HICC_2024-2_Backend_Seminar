from django.urls import path

from . import views # .은 해당 폴더 (accounts) 의미

app_name = 'accounts'

urlpatterns = [
    path('', views.login_view, name = "login"),
	path('register/', views.register, name = "register"),
]