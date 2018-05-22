from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Função apenas para exemplo de saida e retorno entre URLs
def exemplo(request):
    now = datetime.datetime.now()
    html = '<h1>Exemplo de saida %s. </h1>' % now
    return HttpResponse(html)

# Função principal real da aplicação!
def home(request):
    return render(request, 'contas/home.html')
