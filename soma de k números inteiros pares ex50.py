# desenvolva um programa que leia k números inteiros e mostre a soma apenas dos pares. Desconsidere os impares
s = 0
k = int(input('até qual número você quer ir?'))
for a in range(0,k):
    b = int(input('me diga um número'))
    if b % 2 ==0:
        s += b
print(f' a soma dos números é {s}')

