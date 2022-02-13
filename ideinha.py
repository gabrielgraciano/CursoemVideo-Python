#não sei muito bem o que fazer, mas queria um projeto novo em python
import random
min = int(input('dê é o menor valor possível para o número'))
max = int(input('dê o maior valor possível para o número')) 
numero = random.randint(min,max)
while False:
  try:
    guess = int(input('chute um número'))
    if guess > numero:
      print('o número dado é maior do que o número sorteado')
    if guess < numero:
      print('o numero dado é maior do que o número sorteado')
    
