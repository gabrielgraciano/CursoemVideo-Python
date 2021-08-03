# desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética, mostre os 10 primeiros termos
# a partir disso:
a1 = int(input('qual é o primeiro termo da sua progressão?'))
k = int(input('qual é a razão da sua progressão?'))
ultimo = a1 + k * 9
for b in range(a1, ultimo + k, k):
    print(b, end='→ ')
print('fim')
#e se eu quisesse escrever tipo:  o valor para o (n) termo é (x) mas em todas as vezes do laço de repetição???
