print('\033[34mgerador de pa')
a = int(input('termo inicial'))
b = int(input('razao'))
t = a
contador = 1
termofinal = int(input('ate qual termo voce quer ir? '))
while contador < termofinal:
    t = (t + b)
    print(t, end='→ ')
    contador += 1
c = str(input('\nvocê quer continuar?S/N ')).upper().strip()
while c == 'S':
    if c == 'S':
        d = int(input('até qual novo termo você quer ir? '))
        while contador < d:
            t = (t + b)
            contador += 1
            print(t, end='→ ')
        print('\nfim')
    c = str(input('você quer continuar?S/N' )).upper().strip()
else:
    print('fim')
