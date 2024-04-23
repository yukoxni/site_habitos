from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario

def home(request):
    return render(request, 'inicio/home.html')

def cadastro(request):
    if request.method == 'POST':
        primeiro_nome = request.POST.get('firstname')
        sobrenome = request.POST.get('lastname')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        # Verifica se o e-mail já está cadastrado
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'cadastros/cadastro.html', {'erro': 'Este e-mail já está em uso. Por favor, escolha outro.'})
        
        novo_usuario = Usuario(nome=primeiro_nome, sobrenome=sobrenome, email=email)
        novo_usuario.set_senha(senha)
        novo_usuario.save()
        
        # Redireciona para alguma página de sucesso
        return redirect('user_login')
    
    return render(request, 'cadastros/cadastro.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')

        if Usuario.objects.filter(email=email).exists():
            # Se o email existir, redirecionar para a página 'habito'
            return redirect('habito')
        else:
            mensagem = 'O email {} não está cadastrado.'.format(email)
            return render(request, 'login/logar.html', {'mensagem': mensagem})
    
    return render(request, 'login/logar.html')

def habito(request):
    return render(request, 'inicio/habitos.html')