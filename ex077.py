# crie uma tupla com várias palavras. Depois disso mostrar, para cada palavra, quais são suas vogais. Sem acentos
tupla = ('banana', 'pera', 'mouse', 'abacaxi')
for n in tupla:
    print(f'\nNa palavra {n} temos ',end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(f' {letra}',end='')
