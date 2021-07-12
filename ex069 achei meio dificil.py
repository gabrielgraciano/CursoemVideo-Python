# crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# o usuário quer continuar ou não. No final, mostre:
# a) quantas pessoas têm mais de 18 anos;
# b) quantos homens foram cadastrados;
# c) quantas mulheres têm menos de 20 anos
maior = 0
homem = 0
mulher = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('qual é seu sexo? M/F ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print(f' Ao total, {maior} pessoas têm mais de 18 anos, {homem} homens foram cadastrados e {mulher} mulheres têm menos'
      f' de 20 anos.')
# porque se eu coloar resp == '' dá erro?
