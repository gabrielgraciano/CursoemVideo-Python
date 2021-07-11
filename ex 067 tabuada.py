# crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
b = 0
while b >= 0:
    b = int(input('você quer ver a tabuada de qual valor?'))
    if b < 0:
        break
    for a in range(0,11):
        print(f'{a} x {b} = {a * b}')
print('fim')
    # por que quando eu coloco o b = int(input('você quer ver a tabuada de qual valor?')) após o laço dá errado?
