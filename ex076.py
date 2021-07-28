# crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final mostre uma listagem de preços, organizando os dados em forma tabular
tupla = ('caderno', 15.00,
         'lápis', 2.00,
         'caneta', 1.00)
for n in range(0, len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<30}', end=' ')
    else:
        print(f'R${tupla[n]:>6.2f}')
