from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .models import Robo, Cliente, Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.session._session: # verifica se há uma sessão ativa, caso haja, redireciona para página principal
        return redirect('/home/')
    
    return render(request, 'login.html')

def login_submit(request):
    usuario = request.POST.get('usuario') # obtem o usuário digitado
    senha = request.POST.get('senha') # obtem a senha digitada

    user = authenticate(username=usuario, password=senha) # realiza a autenticação

    if user is not None:
        auth_login(request, user) # cria a sessão
        return redirect('/home/')
    else:
        messages.error(request,'Usuário ou senha inválidos') # mostra ao usuário que há erros nas credenciais dele
        return redirect('/')

def sair(request):
    logout(request) # finaliza a sessão
    return redirect("/")

@login_required
def home(request):
    user = request.user

    if user.is_staff: # verifica se o usuário é membro da equipe interna
        return redirect('/admin/') # redireciona para o admin

    cliente = user.cliente # obtem o cliente a partir do usuário
    robos = Robo.objects.filter(cliente = cliente) # obtem os robôs que este cliente possui
    return render(request, 'home.html', {"robos":robos, "cliente":cliente})

@login_required
def robos(request, id):
    user = request.user # obtem o usuário da sessão
    robo = Robo.objects.filter(codigo = id).first() # busca o robo no banco de dados

    if user.cliente.codigo != robo.cliente.codigo: # previne o acesso direto de um usuário que não seja o proprietário do robô
        return redirect("/home/")
    
    return render(request, 'robo.html', {"robo":robo})


