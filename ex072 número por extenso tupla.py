# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte
# Seu programa deverá ler um número do teclado e(entre 0 e 20) e mostrá-lo por extenso
tupla = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um número '))
    
    if num > 20:
        num = int(input('incorreto, digite outro número'))
        while num > 20:
            num = int(input('incorreto, digite outro número'))
            
    posicao = num - 1
    print(f'você digitou o número {tupla[posicao]}')
    break
