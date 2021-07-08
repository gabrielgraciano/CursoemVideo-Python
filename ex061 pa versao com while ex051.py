print('gerador de pa')
a = int(input('termo inicial'))
b = int(input('razao'))
t = a
contador = 1
termofinal = int(input('ate qual termo voce quer ir?'))
while contador <= termofinal:
    t = (t + b)
    print(t, end=' ')
    contador += 1
print('fim')
