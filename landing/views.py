from django.shortcuts import render, redirect
from .models import Aluno, Usuario

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def index(request):
    if request.method == 'POST':
        data_usuario = Usuario()
        data_usuario.email = request.POST['email']
        data_usuario.senha = request.POST['senha']
        data_usuario.save()
        
        data_aluno = Aluno()
        data_aluno.frase = request.POST['frase']
        data_aluno.save()
        # return redirect(request, 'login.html')
    return render(request, 'index.html')

def listar(request):
    listar_frase = Aluno.objects.filter(ativo=True).all()
    contexto = {
        'listar_frase': listar_frase
    }
    return render(request, 'lista.html', contexto)

def deletar(request):
    item = Aluno.objects.get(id=id)
    if item is None:
        item.ativo= False
        item.save()
        return redirect('/aluno/listar')
    return render(request, 'lista.html')

def login(request):
    if request.method == 'POST':
        data_aluno = Usuario()
        data_aluno.email = request.POST['email']
        data_aluno.senha = request.POST['senha']
        data_aluno.save()
    return render(request, 'login.html')