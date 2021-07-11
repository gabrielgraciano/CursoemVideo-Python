# faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER
# mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
import random as rd
print('VAMOS JOGAR PAR OU ÍMPAR')
num = 0
cont = 0
start = 0
while start == 0:
    opc = str(input('você quer par ou ímpar? P/I')).upper().strip()
    num = int(input('escolha um número entre 0 e 10'))
    numpc = rd.randint(0,10)
    soma = num + numpc
    if num > 10:
        break
    if opc == 'P':
        if soma % 2 == 0:
            print('você ganhou!')
            cont += 1
        elif soma % 2 != 0:
            print('você perdeu')
            break
    if opc == 'I':
        if soma % 2 == 0:
            print('você perdeu')
            break
        elif soma % 2 != 0:
            print('você ganhou')
            cont += 1
print(f' você ganhou {cont} vezes!')
