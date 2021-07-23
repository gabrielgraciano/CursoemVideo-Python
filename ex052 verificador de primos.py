# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('digite um número'))
b = 0
for a in range(1, n + 1):
    if n % a == 0:
        print('\033[33m', end='')
        b += 1
    else:
        print('\033[31m', end='')
    print(f'{a} ', end='')
print('\n\033[m'f' o número {n} foi divisível {b} vezes')
if b == 2:
    print('\033[34mlogo, ele é primo')
else:
    print('\033[34mportanto, ele não é primo')
