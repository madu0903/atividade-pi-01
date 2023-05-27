from django.shortcuts import render
from .models import Filmes, Locacao

# Create your views here.
def index_view(request):
    return render(request,'locadora/index.html')

def filmes_view(request):
    lista_filmes=Filmes.objects.all()
    context={'filmes':lista_filmes}
    return render(request,'locadora/filmes.html',context)

def locacoes_view(request):
    lista_locacao=Locacao.objects.all()
    context={'locacoes':lista_locacao}
    return render(request,'locadora/locacao.html',context)