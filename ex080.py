''' crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela '''
lista = []
for a in range(0,5):
    n = int(input('digite um valor ' ))
    if a == 0 or n > lista[len(lista) -1]:
        lista.append(n)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado à posição {pos} da lista')
                break
            pos += 1
print(lista)
