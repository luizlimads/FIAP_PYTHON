from funct1 import *

nome = 'Luizlimads'
data = '19 jan 2022'
linguagem = 'python'
print(nome,' está treinando em', linguagem,'--',data)
print('=========================================================')
print('Tomada de decisao e estrutura de repeticao')
valor = input('Digite um número pertencentes aos naturais para ver sua representacao em binario, ou exit para sair: ')
while valor != 'exit':
    if valor == 'random':
        print('aleatorio')
        repetir()
    else:
        print('com seus dados')
        testeFinal(valor)
    valor = input('\nexit para sair e random para numeros aleatorios \n')

print('fim')
    