from yoursite.models import Usuarios
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvar os dados no banco de dados
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # Exibir todos os usuarios cadastrados em uma janela
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }

    #retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)