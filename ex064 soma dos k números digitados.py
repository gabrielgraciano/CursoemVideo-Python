# crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
# 999, que é condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsidere a flag)
k = 0
j = 0
c = 0
while k != 999:
    k = int(input('digite um número'))
    if  k != 999:
        j += k
        c += 1
print(f'A soma dos números é {j}, e você digitou {c} números')
