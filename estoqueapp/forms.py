from django import forms
from .models import Estoque

class EstoqueFormCreate(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['categoria', 'nome_item', 'quantidade', 'quantidade_emitida', 'emitido_por', 'emitido_para', 'numero_telefone']