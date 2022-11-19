"""Criar um programa que gera uma sequência de 1000 números aleatóriamente. 
Estes números devem ser gerados entre 0 e 10.000. 
Depois o programa deve limpar todos os números repetidos e mostrar na tela a quantidade de números que foram utilzados sem
 repetição.
 """
from random import randint
numeros = []
for i in range(1000):
    numeros.append(randint(0,10000))
print(numeros)
print(len(numeros))
s = set(numeros)
print(s)
print(len(s))