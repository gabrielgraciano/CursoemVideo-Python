# crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final, mostre:
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de 1000 reais;
# C) Qual é o nome do produto mais barato.
total = caro = barato = cont = 0
maisbarato = ' '
while True:

    prod = str(input('qual o nome do produto comprado? '))
    preco = int(input('quanto custa? R$'))
    cont += 1
    total += preco

    if cont == 1:
        barato = preco

    if preco >= 1000:
        caro += 1
    else:
        if preco < barato:
            barato = preco
            maisbarato = prod

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('você quer continuar? S/N ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f' Você gastou R${total} na compra, {caro} produtos custam mais de mil reais e o produto mais barato é {maisbarato}, '
      f'que custou R${barato} reais')
