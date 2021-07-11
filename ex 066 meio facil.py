num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('digite um número'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} números é {soma}')
