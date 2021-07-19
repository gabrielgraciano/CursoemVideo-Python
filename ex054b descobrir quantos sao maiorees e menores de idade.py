#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
n = int(input('de quantas pessoas estamos falando?'))
maior = 0
menor = 0
for pessoa in range(1,n + 1):
    nasc = int(input(f'em que ano nasceu a {pessoa}ª em questão?'))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f' O espaço amostral constituído por {n} pessoas tem {maior} maiores de idade e {menor} menores de idade')
