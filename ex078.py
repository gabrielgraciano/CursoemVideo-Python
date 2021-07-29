# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.
lst = []
c = 1
for a in range(0, 5):
    b = int(input(f'digite um valor para a posição {c} '))
    lst.append(b)
    c += 1
print(f'O maior valor da lista é {max(lst)} e sua posição é a {lst.index(max(lst)) + 1}ª, o menor é  {min(lst)}'
      f' e sua posição é a {lst.index(min(lst)) + 1}ª')
