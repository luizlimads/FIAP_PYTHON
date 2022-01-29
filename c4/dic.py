from func import *
ips = {}
resp="S"
while resp=="S":
    escolha()
    chave = input('Site a ser buscado: ')
    ips[chave] = ipDNS(chave)
    resp=input("Digite <S> para continuar: ").upper()

print(ips)