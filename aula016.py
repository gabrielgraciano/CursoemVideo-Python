lanche = 'hambúguer', 'suco', 'pizza', 'pudim'

for comida in lanche:
    print(f'eu vou comer {comida}')

for cont in range (0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')

# ou também poderia ser
# for comida in lanche:
#   print(comida)

a = (1, 2, 3)
b = (3, 4, 5, 6, 7)
c = a + b
print(c)
d = b + a
print(d)
print(c.count(2)) # assim ele printa quantas vezes o número 2 aparece
print(c.index(5)) # irá mostrar em que posição da tupla está o número 5
print(c.index(3, 3)) #irá contar a posição do 2 a partir do terceiro elemento da tupla(justo odne está o segundo 3

del(d) #irá deletar a tupla d, isso serve para deletar qualquer coisa em python
