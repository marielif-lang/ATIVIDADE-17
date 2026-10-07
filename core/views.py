from django.shortcuts import render, get_object_or_404
from .models import Projeto

# Tela de Listagem de Projetos
def lista_projetos(request):
    projetos = Projeto.objects.all()
    context = {
        'projetos': projetos
    }
    return render(request, 'core/lista_projetos.html', context)

# Tela de Detalhes do Projeto (recebe id)
def detalhe_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id)
    context = {
        'projeto': projeto
    }
    return render(request, 'core/detalhe_projeto.html', context)