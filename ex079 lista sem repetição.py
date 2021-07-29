''' Faça um programa onde o usuário pode inserir valores numéricos e cadastrar numa lista.
Caso o número já exista lá, ele não será adicionado. No final serão exibidos todos os valores únicos digitados
em ordem crescente '''
lst = []

while True:

    a = int(input('Qual número você quer cadastrar? '))
    if a not in lst:
        lst.append(a)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('você quer continuar? S/N ')).upper().strip()
    if resp == 'N':
        break

lst.sort()
print(lst)

# '''por que eu não posso colocar resp = ''? dá erro'''
# por que se eu colocasse print(lst.sort()) daria erro 'None'?
