# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# a) quantos vezes apareceu o valor 9
# b) em que posição foi digitado o primeiro valor 3
# c) quais foram os números pares
nove = par = 0
num = (int(input('digite um número')), int(input('digite um número')), int(input('digite um número')),
int(input('digite um número')))

print(f'o número 9 aparece {num.count(9)} vezes')

if 3 in num:
    print(f'o número 3 aparece {num.index(3)}')

for n in num:
    if n % 2 == 0:
        par += 1
        print(n, end= ' ')

print(f'\n {par}números são pares')
