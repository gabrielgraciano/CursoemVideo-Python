# crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior algarismo
# [4] novos números
# [5] sair do programa
print('''\033[34m
    Tem-se as seguintes opções:
   [1] Somar
   [2] Multiplicar
   [3] Maior algarismo
   [4] Novos números
   [5] Sair do programa\033[m''')
print()
a = int(input('\033[35mdigite um número '))
print()
b = int(input('digite outro \033[m'))
c = 0
while c != 5:
    c = int(input('\033[37mescolha uma das opções\033[m '))
    if c == 1:
        print(f'\033[36m a soma entre os números é {a + b}')
    elif c == 2:
        print(f'\033[36m a multiplicação entre os números é {a * b}')
    elif c == 3:
        if a > b:
            print(f'\033[36m o maior número é {a}')
        elif a < b:
            print(f'\033[36mo maior algarismo é {b}')
        else:
            print('\033[36mos algarismos são iguais')
    elif c == 4:
        a = int(input('\033[35mdigite um número'))
        b = int(input('\033[35mdigite outro'))
print('nos vemos na próxima')
