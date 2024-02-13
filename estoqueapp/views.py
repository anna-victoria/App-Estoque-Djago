from django.shortcuts import render, redirect
from .models import Estoque
from .forms import EstoqueFormCreate, EstoqueFormSearch


# Create your views here.
def home(request):
	title = 'Página Inicial, bem vindo(a)!'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)

def listar_produtos(request):
    title = 'Lista de Produtos'
    form = EstoqueFormSearch(request.POST or None)
    queryset = Estoque.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Estoque.objects.filter(categoria__icontains=form['categoria'].value(), nome_item__icontains=form['nome_item'].value())
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        } 
    return render(request, "listar_produtos.html", context)


def adicionar_produtos(request):
    form = EstoqueFormCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/listar_produtos')
    
    context = {
        "form": form,
        "title": "Adicionar um produto",
    }
    return render(request, "adicionar_produtos.html", context)
