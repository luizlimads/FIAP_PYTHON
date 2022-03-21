import time
from os import sep
import socket
import ast
from datetime import datetime

doc = 'arqEx.txt'

def verificarArq(doc):
    try:
        with open(doc,'r') as arquivo:
            conteudo = arquivo.read()            
    except FileNotFoundError:
        with open(doc,'a') as arquivo:
            conteudo = arquivo.write('{}')        
    parsed_json = ast.literal_eval(str(conteudo))
    return(parsed_json)    

def lerSite(doc):
    conteudo = verificarArq(doc)
    print(*conteudo.keys(),sep='\n')
        
def inserirSite(doc):
    conteudo = verificarArq(doc)
    condicaoFuncao = True
    while condicaoFuncao :
        if condicaoFuncao:
            condicaoPergunta = True
        site = input('Digite o site a ser inserido: ')
        literal = eval('{"'+site+'":[]}')
        conteudo.update(literal)
        while condicaoPergunta:
            valor = input('Digite sua escolha:\n \
    1 para inserir novo site\n \
    2 para ver a lista de sites\n \
    3 para encerar operacao:\n \
    Opcao escolhida: ')
            if valor == '1':
                condicaoPergunta = False
            elif valor == '2':
                print(*conteudo.keys(),sep='\n')
            elif valor == '3':
                condicaoFuncao = False
                condicaoPergunta = False
            else:
                print('\n Valor nao encontrado \n')
    with open(doc,'w') as arquivo:
        arquivo.write(str(conteudo))    

def apagarSite(doc):
    conteudo = verificarArq(doc)
    condicaoFuncao = True
    while condicaoFuncao:
        if condicaoFuncao:
            condicaoPergunta = True
        site = input('Digite o site a ser removido: ')
        conteudo.pop(site)
        while condicaoPergunta:
            valor = input('Digite sua escolha:\n \
    1 para excluir um site\n \
    2 para ver a lista de sites\n \
    3 para encerar operacao:\n \
    Opcao escolhida: ')
            if valor == '1':
                condicaoPergunta = False
            elif valor == '2':
                print(*conteudo.keys(),sep='\n')
            elif valor == '3':
                condicaoFuncao = False
                condicaoPergunta = False
            else:
                print('\n Valor nao encontrado \n')    
    print(*conteudo.keys(),sep='\n')
    with open(doc,'w') as arquivo:
        arquivo.write(str(conteudo))

def informacaoSites(doc):
    conteudo = verificarArq(doc)
    siteApontar = list(conteudo.keys())
    infos = []
    for i in siteApontar:
        try:
            ip = socket.gethostbyname(i)            
        except socket.error :
            print('\n')     
        time.sleep(.5)
        novasInformacoes = {'ip':ip,'data':datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
        infos.append(novasInformacoes)
        conteudo.get(i).append(novasInformacoes)
    for l in range(len(siteApontar)):
        print(siteApontar[l]+': '+infos[l].get('ip'))        
    with open(doc,'w') as arquivo:
        arquivo.write(str(conteudo))

def verInfos(doc):
    conteudo = verificarArq(doc)
    siteApontar = list(conteudo.keys())
    for l in siteApontar:
        print('\n')
        print(l)
        print(*list(i for i in conteudo.get(l)),sep='\n')



def escolha():
    doc = 'arqEx.txt'
    valor = input('digite umas das opcoes:\n \
     1 ler sites\n \
     2 inserir novo site\n \
     3 apagar site especifico\n \
     4 obter informacoes dos sites\n \
     5 ver informaçôes\n \
opcao escolhida: ')    
    return valor 

