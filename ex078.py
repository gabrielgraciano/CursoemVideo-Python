'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.
'''
lst = []
for a in range(5):
    b = int(input('digite um número '))
    lst.append(b)

print(f'A lista digitada é {lst}.')

print(f'O maior valor é {max(lst)} e está nas posições ',end='')

for indice, valor in enumerate(lst):
    if valor == max(lst):
        print(f'nas posições {indice + 1}. O menor valor é {min(lst)} nas posições ', end='')

for indice, valor in enumerate(lst):
    if valor == min(lst):
        print(f'{indice + 1}')
