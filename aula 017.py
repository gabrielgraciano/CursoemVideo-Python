# Listas
# Listas são mutáveis, usa-se colchetes []
lanche = ['a', 'b', 'c']
lanche[2] = 'd'

# Comandos para adicionar elementos à lista
print(lanche) # listas permitem a troca de itens

lanche.append('f') #adicionou-se f à lista
print(lanche)

lanche.insert(1, 'e')
print(lanche) #adicionou-se na posição 1 o elemento 'e'. Todos os outros acima de 1 moveram uma casa

# Comandos para deleção:
del lanche[2] #irá deletar a posição 2
lanche.pop(2) #irá deletar a posição 2. lanche.pop() irá remover o último elemento necessariamente
if 'b' in lanche:
    lanche.remove('b') #irá deletar b (que está na posição 2). Caso haja mais de um, removerá só o primeiro
    # Caso não houvesse 'b' e tentasse se deletar 'b' sem o operador in, daria erro
# Obs.: Após a deleção, os índices são reformulados

valores = list(range(4, 11)) #cria uma lista no range de 4 a 10
valores2 = [0, 2, 5, -1, 27, 6, 5]
valores2.sort() #irá organizar por ordem crescente
print(valores2)
print(valores2.sort(reverse=True)) #irá printar na ordem inversa


lista = []
lista.append(1)
lista.append(3)
lista.append(9)
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}')


a = [1, 3, 4, 5]
b = a
print(a)
print(b)
b[2] = 9
print(a)
print(b)
print()
# quando você iguala listas elas ficam para sempre conectadas, qualquer mudança em uma mudará na outra

# para criar uma cópia não interligada deveria-se fazer o seguinte: o ':' pega tooodos os elementos de a
b = a[:]
b[2] = 78
print(a)
print(b)
