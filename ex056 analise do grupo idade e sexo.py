# desenvolva um programa que leia o nome idade e sexo de n pessoas. No final ele deve mostrar:
# -a média de idade do grupo
# -Qual é o homem mais velho
# -Quantas mulheres têm menos de 20 anos
homem = []
H = 0
M = 0
N = 0
maior = 0
menor = 0
media = 0
n = int(input('de quantas pessoas estamos falando?'))
for a in range(n):
    print('####################################')
    print()
    b = str(input('qual é o nome dessa pessoa?'))
    c = int(input('qual é a idade dessa pessoa?'))
    d = str(input('qual o sexo dessa pessoa? responda com masculino ou feminino'))
    print()
    homem = [b]
    if d == 'masculino':
        H += 1
        media += c
        if a == 1:
            maior = c
            menor = c
        else:
            if c > maior:
                maior = c
                homem.clear()
                homem.append(b)
            if c < menor:
                menor = c
    if d == 'feminino':
        M += 1
        media += c
        if c < 20:
            N += 1
e = media/n
print(f' A média de idade do grupo é de {e} anos, o homem mais velho é o {homem[0]}, e ele tem {maior} anos.'
      f'Além disso, {N} mulheres tem menos de 20 anos')
