from django.shortcuts import render, redirect
from .models import Estoque
from .forms import EstoqueFormCreate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
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
        return redirect('/listar_produtos')
    
    context = {
        "form": form,
        "title": "Adicionar um produto",
    }
    return render(request, "adicionar_produtos.html", context)

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_produtos')
        else:
            form = UserCreationForm()
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
