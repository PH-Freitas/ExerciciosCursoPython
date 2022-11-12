"""Fazer um programa em que o usuário entra com uma palavra e o programa printa na tela letra por letra separadamente.

Por exemplo: Abacate

A

b

a

c

a

t

e
"""

palavra = input("Digite uma palavra\n")
i = 0
contador = 0
sep = len(palavra)
while contador < sep:
   a = palavra[i]
   print(a)
   i+=1
   contador+=1