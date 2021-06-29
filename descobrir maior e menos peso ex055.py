# faça um programa que leia o peso de n pessoas e diga qual deles é o mais pesado e qual é o mais leve
list = []
a = int(input('de quantas pessoas estamos falando?'))
for b in range(a):
    c = float(input('qual é o peso da pessoa em quilos?'))
    list.append(c)
print(f' o menor peso é de {min(list)} kg e o maior peso é de {max(list)} kg')
# como eu faria caso eu quisesse que ele perguntasse o nome de cada pessoa, seu peso e em seguida montasse
# um esquema em ordem decrescente de peso (ou em ordem alfabética)?
