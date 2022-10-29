"""Fazer um programa em que:

1. Usuário entra com 3 números (x, y e z)

2. Imprime na tela x + y

3. Imprime na tela x elevado a z

4. Imprime a subração x - y - z
"""
x = int(input("Digite o primeiro numero:\n"))
y = int(input("Digite o segundo numero:\n"))
z = int(input("Digite o terceiro numero:\n"))
soma = x + y
elevado = x**z
subtração = x - y - z
print("{} + {} = {}".format(x,y,soma))
print("{} ** {} = {}".format(x,z,elevado))
print("{} - {} - {} = {}".format(x,y,z,subtração))