import linecache
import socket
import re



def ipDNS(chave):
    valueChave = (chave,socket.gethostbyname(chave))
    return(valueChave)

def escolha():
    valor = input('digite umas das opcoes:\n \
     1 verificar sites\n \
     2 inserir novo site\n \
     3 apagar site especifico\n \
     4 obter informacoes dos sites\n \
opcao escolhida: ')
    return valor 

doc = 'arqEx.txt'
def verificarArq(doc):
    try:
        with open(doc,'r') as arquivo:
            linhas = len(arquivo.readlines())
            conteudo = arquivo.read()
    except FileNotFoundError:
        with open(doc,'a') as arquivo:
            linhas = 3
            conteudo = arquivo.write('{\n \n }')
    return({conteudo,linhas})        

def lerArq(doc):
    print(verificarArq(doc))

def inserirSite(doc):
    verificarArq(doc)
    with open(doc,'r') as arquivo:
        # conteudo = arquivo.write('algo\n')
        conteudo = arquivo.readlines()
        # print(conteudo)
        # print(type(conteudo[0]))
        len(conteudo)
        print(len(conteudo))
        # c= ' '.join(conteudo)
        # len(re.findall('\n',c))
        # print(len(re.findall('\n',c)))

            
