from random import randint
from time import sleep

def repetir():
    for i in range(0,10**5,1):
        valor = randint(0,10e3)
        transformaBinario(valor)
        sleep(.1)

def transformaBinario(valor):
    aux1 = [int(valor)]
    aux2 = []
    while (aux1[-1]>0):
        aux2.insert(0,aux1[-1] % 2)
        aux1.append(aux1[-1] // 2)
    print(''.join(map(str,aux2)),end=' ')

def testeFinal(valor):
    try:
        int(valor)
        valor = int(valor)
        transformaBinario(valor)
    except:
        print('Valor nao reconhecido')