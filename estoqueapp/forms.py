from django import forms
from .models import Estoque

class EstoqueFormCreate(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['categoria', 'nome_item', 'quantidade', 'quantidade_emitida', 'emitido_por', 'emitido_para', 'numero_telefone']
        
class EstoqueFormSearch(forms.ModelForm):
    categoria = forms.CharField(required=False)
    nome_item = forms.CharField(required=False)
    class Meta:
     model = Estoque
     fields = ['categoria', 'nome_item']
     