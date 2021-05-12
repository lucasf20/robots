from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.session._session: #verifica se há uma sessão ativa
        return redirect('/home/')
    
    return render(request, 'login.html')

def login_submit(request):
    usuario = request.POST.get('user')
    senha = request.POST.get('password')

    user = authenticate(username=usuario, password=senha)

    if user is not None:
        auth_login(request, user)
        return redirect('/home/')
    else:
        messages.error(request,'Usuário ou senha inválidos')
        return redirect('/')

def home(request):
    return render(request, 'home.html')

