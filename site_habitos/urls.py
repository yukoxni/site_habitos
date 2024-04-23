from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.user_login, name= 'user_login'),
    path('habito/', views.habito, name='habito'),
]
