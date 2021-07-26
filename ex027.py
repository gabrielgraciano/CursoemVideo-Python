a = str(input('Digite seu nome completo')).strip()
b = a.split()
c = b[len(b) - 1]
print(f'Seu primeiro nome é {b[0]} e seu último nome é {c}')
