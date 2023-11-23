from django.shortcuts import render

# Create your views here.
def home(request):
	title = 'Página Inicial, bem vindo(a)!'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)