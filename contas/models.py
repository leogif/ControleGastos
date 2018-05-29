from django.db import models

# Classe que implementa o nome da nossa categoria de contas
class Categoria(models.Model):
    nome = models.CharField(max_length=250)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Transacaoes(models.Model):
    data = models.DateTimeField()
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacoes'
