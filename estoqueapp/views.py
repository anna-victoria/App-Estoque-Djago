from django.shortcuts import render
from .models import Estoque
from .forms import EstoqueFormCreate

# Create your views here.
def home(request):
	title = 'Página Inicial, bem vindo(a)!'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def listar_produtos(request):
    title = 'Lista de Produtos'
    queryset = Estoque.objects.all()
    context = {
    "title": title,
    "queryset": queryset,
    }
    return render(request, "listar_produtos.html",context)

def adicionar_produtos(request):
	form = EstoqueFormCreate(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		"form": form,
		"title": "Adicionar um produto",
	}
	return render(request, "adicionar_produtos.html", context)