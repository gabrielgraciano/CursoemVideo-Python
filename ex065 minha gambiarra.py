# crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar os valores
a = 'S'
soma = 0
cont = 0
soma1 = 0
lst = []
while a == 'S':
    num = int(input('digite um número'))
    soma1 += num
    cont += 1
    lst.append(num)
    a = str(input('você quer continuar? s/n')).strip().upper()
g = soma1/cont
print(f'A soma dos números é {soma1}, a média dos {cont} números digitados é {g}. O maior número digitado é {max(lst)} e'
      f'o menor é {min(lst)}')
