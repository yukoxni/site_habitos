from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario

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
        return redirect('login')
    
    return render(request, 'cadastros/cadastro.html')

def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')

        # Autentica o usuário
        usuario = authenticate(request, email=email, password=senha)
        
        if usuario is not None:
            # Autentica e faz login do usuário
            login(request, usuario)
            return render(request, 'inicio/index.html')
        else:
            # Credenciais inválidas, exibir mensagem de erro
            messages.error(request, 'E-mail ou senha incorretos. Tente novamente.')

    return render(request,'login_usuario/logar.html')

def habito(request):
    return render(request, 'inicio/index.html')