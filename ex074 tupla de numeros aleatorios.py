# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois mostre a listagem desses núme-
# ros e também indique o maior e o menor número.
from random import randint
tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),)
for i in tupla:
    print(i, end=' ')
print(f'\nO maior valor é {max(tupla)} e o menor valor é {min(tupla)}')
