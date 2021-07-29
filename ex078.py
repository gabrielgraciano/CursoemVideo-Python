# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.
lst = []
for a in range(0, 5):
    b = int(input('digite um valor '))
    lst.append(b)
print(f'O maior valor da lista é {max(lst)} e sua posição é a {lst.index(max(lst)) + 1}ª, o menor é  {min(lst)}'
      f' e sua posição é a {lst.index(min(lst)) + 1}ª')
