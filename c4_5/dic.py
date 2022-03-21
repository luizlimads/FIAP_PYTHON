from func import *
resp="S"
while resp=="S":
    valor = escolha()
    if valor == '1':
        lerSite(doc)
        print('\n')
    elif valor == '2':
        inserirSite(doc)        
    elif valor == '3':
        apagarSite(doc)
    elif valor == '4':
        informacaoSites(doc)
    elif valor == '5':
        verInfos(doc)
    else:
        print('Nao encontrado')
        resp=input("Digite <S> para continuar: ").upper()
