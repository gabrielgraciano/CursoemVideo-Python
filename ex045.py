# :crie um programa que jogue jokempô com o computador
# : 1 = pedra   2 = papel   3 = tesoura
import random
print('\033[36m-=' * 25)
print()
print('\033[33m vamos jogar jokempô')
print()
print('\033[36m-=' * 25)
a = random.randint(1,3)
b = str(input('\033[33m vc escolhe pedra, papel ou tesoura?')).strip().lower()
if a == 1 and b == 'pedra':
    print('empatou')
elif a == 1 and b == 'papel':
    print( 'vc ganhou!!')
elif a == 1 and b == 'tesoura':
    print('o pc ganhou amg')
elif a == 2 and b == 'pedra':
    print('o pc ganhou')
elif a == 2 and b == 'papel':
    print('empatou')
elif a == 2 and b == 'tesoura':
    print('vc ganhou')
elif a == 3 and b == 'pedra':
    print('vc ganhou')
elif a == 3 and b == 'papel':
    print('o pc ganhou')
elif a == 3 and b == 'tesoura':
    print('empatou')