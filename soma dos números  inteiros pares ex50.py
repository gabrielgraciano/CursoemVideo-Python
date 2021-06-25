# desenvolva um programa que leia seis números inteiros e mostre a soma apenas dos pares. Desconsidere os impares
s = 0
for a in range(0,6):
    b = int(input('me diga um número'))
    if b % 2 ==0:
        s = 0 + b
print(f' a soma dos números é {s}')

