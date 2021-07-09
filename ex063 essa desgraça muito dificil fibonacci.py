# escreva um programa que leia um numero k inteiro qualquer e mostre na tela os k primeiros elementos de uma sequencia de
# fibonacci.
# seq fib = 1 1 2 3 5 8
print('~' * 30)
print('SEQUÊNCIA DE FIBONACCI')
k = int(input('até qual termo da sequência você quer ir?'))
a = 3
t1 = 1
t2 = 1
t3 = t1 + t2
print('1 1', end=' ')
while a <= k:
    t3 = t2 + t1
    a += 1
    t1 = t2
    t2 = t3
    print(t3, end=' ')
print()
print('~' * 30)
# print(end='\n') seria outra forma de quebrar a linha
# print('~'* 30)
