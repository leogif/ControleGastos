from django.forms import ModelForm
from .models import Transacaoes


class TransacaoForm(ModelForm):
    class Meta:
        model = Transacaoes
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']
        
