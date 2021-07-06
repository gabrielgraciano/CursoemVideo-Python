# faça um programa que leia um número qualquer e mostre o seu fatorial
from math import factorial as f
print('VAMOS CALCULAR FATORIAISSSSSSSSSSS')
a = 0
while a !=2:
    a = int(input('''Qual das opções você quer?
        [1] Calcular fatorial
        [2] Sair do programa
         '''))
    if a != 2:
        n = int(input('Digite o número do fatorial'))
        if n < 0:
            print('Não existe fatorial menor que 0')
        elif n == 0:
            print('O fatorial de 0 é 1')
        else:
            c = f(n)
            print(f'O valor do fatorial em questão é {c}')
print('Fim')
