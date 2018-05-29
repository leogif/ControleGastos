from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Função apenas para exemplo de saida e retorno entre URLs
def exemplo(request):
    now = datetime.datetime.now()
    html = '<h1>Exemplo de saida %s. </h1>' % now
    return HttpResponse(html)

# Função para exemplos da aplicação!
def home(request):
    now = datetime.datetime.now()
    transacao = ['transacao 1', 'transacao 2', 'transacao 3']
    dic = { 'now':now , 'transacao':transacao }
    return render(request, 'contas/home.html', dic)
