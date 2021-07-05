# melhore o jogo do exercício 028, o jogador deve jogar até acertar e o jogo deve mostrar quantas tentativas foram necessárias
import random
a = random.randint(1,10)
b = ''
c = 0
while b!= a:
    b = int(input('\033[33mme fala um número'))
    c += 1
print(f'Parabéns, você acertou! Foram necessárias {c} jogadas')
