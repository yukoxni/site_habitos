from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.cadastro, name= 'cadastro'),
    path('login/', views.login_usuario, name= 'login'),
    path('habitos/', views.habito, name='habitos')
]
