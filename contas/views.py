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
# Formulario gerado automaticamente e será reaproveitado na função atualizar
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

# Função que realiza a atualização de itens no modelo com base em formulario
# Recebe o ID de um item através de sua Primary Key (pk)
# Cria um formulario preenchido com os valores presentes no modelo refrente
def update(request, pk):
    transacao = Transacaoes.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    data = {}
    # verifica se o dados estão validos e salva no banco retornando a listagem
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    # envia um dicionario para o template com os dados do formulario
    data['form'] = form
    data['transacao'] = transacao
    return render(request, 'contas/form.html', data)

# Função que executa a exclusão de um registro no modelo
# Verifica no template se o registro já existe. Caso exista executa sua exclusão
def delete(request, pk):
    transacao = Transacaoes.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
