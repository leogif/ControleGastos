from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacaoes
from .form import TransacaoForm
import datetime


# Função apenas para exemplo de saida e retorno entre URLs
# Nesse exemplo retornamos o html dentro do HttpResponse
def exemplo(request):
    now = datetime.datetime.now()
    html = '<h1>Exemplo de saida %s. </h1>' % now
    return HttpResponse(html)

# Função para exemplos da aplicação!
# Nesse exemplo fazemos a renderização de um template
def home(request):
    now = datetime.datetime.now()
    transacao = ['transacao 1', 'transacao 2', 'transacao 3']
    dic = { 'now':now , 'transacao':transacao }
    return render(request, 'contas/home.html', dic)


# ------- Conjunto de funções aplicaveis do nosso estudo ------
# Função de chamada para pagina principal da aplicação
def listagem(request):
    data = {}
    data['transacoes'] = Transacaoes.objects.all()
    return render(request, 'contas/listagem.html', data)

# Função que monta e ativa a validação de nosso formulario
# Cria uma instancia do nosso form no template e salva os dados no modelo
def novatransacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    # verifica se o dados estão validos e salva no banco retornando a listagem
    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    # envia um dicionario para o template com os campos do formulario
    data['form'] = form
    return render(request, 'contas/form.html', data)
