from django.contrib import admin
from .models import Estoque
from .forms import EstoqueFormCreate

# Register your models here.

class EstoqueAdminCreate(admin.ModelAdmin):
    list_display = ['categoria', 'nome_item', 'quantidade', 'quantidade_emitida', 'emitido_por', 'emitido_para', 'numero_telefone']
    form = EstoqueFormCreate
    
    # filtrar_lista = ['categoria']
    campo_pesquisa = ['categoria', 'nome_item', 'quantidade', 'quantidade_emitida', 'emitido_por', 'emitido_para', 'numero_telefone']
    search_fields = campo_pesquisa
    # Additional customization options can be added here

admin.site.register(Estoque, EstoqueAdminCreate)