# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
# a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
c = v = d = u = 0


while True:
    sacado = int(input('Quanto você tem ai? R$'))
    # como eu faria para fazer o programa pedir o valor até obter uma entrada númerica, não travar com strings

    if sacado // 50 != 0:
        cinq = sacado // 50
        sacado = sacado - cinq * 50
        c = cinq
    else:
        c = 0

    if sacado // 20 != 0:
        vint = sacado // 20
        sacado = sacado - vint * 20
        v = vint
    else:
        v = 0

    if sacado // 10 != 0:
        dez = sacado // 10
        sacado = sacado - dez * 10
        d = dez
    else:
        d = 0

    if sacado // 1 != 0:
        um = sacado // 1
        sacado = sacado - um * 1
        u = um
    else:
        u = 0

    if sacado == 0:
        print(f'Ao total, você recebe {c} notas de R$50, {v} notas de R$20, {d} notas de R$10 e {u} notas de R$1')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('você quer continuar? S/N')).strip().upper()[0]
    if continuar == 'N':
        break
