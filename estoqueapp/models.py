from django.db import models

# Create your models here.

class Estoque(models.Model):
    categoria = models.CharField(max_length=50, blank=True, null=True)
    nome_item = models.CharField(max_length=50, blank=True, null=True)
    quantidade = models.IntegerField(default='0', blank=True, null=True)
    quantidade_recebida = models.IntegerField(default='0', blank=True, null=True)
    recebido_por = models.CharField(max_length=50, blank=True, null=True)
    quantidade_emitida = models.IntegerField(default='0', blank=True, null=True)
    emitido_por = models.CharField(max_length=50, blank=True, null=True)
    emitido_para = models.CharField(max_length=50, blank=True, null=True)
    numero_telefone = models.CharField(max_length=50, blank=True, null=True)
    criado_por = models.CharField(max_length=50, blank=True, null=True)
    nivel_reposicao = models.IntegerField(default='0', blank=True, null=True)
    ultima_atualizacao = models.DateTimeField(auto_now_add=False, auto_now=True)
    exportar_para_CSV = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_item
