# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
a = str(input('me diga uma frase ai')).strip().upper()
b = a.split()
c = ''.join(b)
d = ''
for e in range(len(c) - 1,-1,-1):
    d += c[e]
print(d, c)
if d == c:
    print('palindromo')
else:
    print('não é palindromo')