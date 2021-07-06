n = int(input('digite um número'))
res = 1
if n < 1:
    print('não existe fatorial de número menor que 1')
elif n == 0:
    print('o fatorial de 0 é 1')
for i in range(1, n+1):
    res = res * i
print(f' o valor do fatorial de {n} é {res}')
