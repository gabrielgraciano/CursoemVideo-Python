# crie um simulador k dados de n lados que pergunte ao usuário se quer rodar ou não e que não seja interrompido por
# entradas não previstas. O script só deve parar caso o usuário não queira mais rodar
import random
print('Olá, sou um programa que simula um dado!')
a = str(input('Você gostaria de rodar dados?'))
if a == 'sim':
    lst = []
    b = int(input('quantos dados você quer rodar?'))
    for c in range(b):
        d = int(input('Você quer um dado de quantos lados?'))
        e = random.randint(1, d)
        lst.append(e)
    for x in range(len(lst)):
        print(f' Os dados são:{lst[x]}', end=' ')
else:
    print('Ok! Nos vemos na próxima')
