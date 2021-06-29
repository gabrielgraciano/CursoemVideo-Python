# faça um programa que leia o peso de n pessoas e diga qual deles é o mais pesado e qual é o mais leve
maior = 0
menor = 0
for a in range(1,6):
    peso = float(input(f'qual é o peso da {a} pessoa?'))
    if a == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f' O maior peso é de {maior} Kg e o menor peso é de {menor} kg')