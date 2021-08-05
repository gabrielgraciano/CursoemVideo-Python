# faça um programa que leia o sexo de uma pessoa, mas só aceita M ou F. Caso esteja errado, peça a digitação novamente
# até ter um valor correto
a = ''
while a != 'M' and a != 'F':
    a = str(input('Qual o seu sexo?')).upper().strip()
print(f'O sexo escolhido foi o {a}')
