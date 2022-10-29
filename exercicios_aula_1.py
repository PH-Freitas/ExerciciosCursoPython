# -*- coding: utf-8 -*-
"""Exercicios_aula_1.ipynb

#PRIMEIRA AULA DE PYTHON

## Comando PRINT

###1. Fazer um programa que escreve na tela Olá Mundo!
"""

print("Olá Mundo!")

"""###2. Concatenando informações """

# Texto e números
print(40 , "anos")

# Texto com booleano
print("Verdadeiro =" , True)

# Textos longos, com mais de uma linha
print('Professor, voce é ' + 25 * " muito " + 'legal')

"""## Tipos de variáveis

###1. Número Inteiro
"""

# Decalarar a Variável Inteira
variavel_inteira = 10

# Imprimir as variáveis na tela (usar .format)
print(variavel_inteira)
print("O numero é: {}".format(variavel_inteira))

"""###2. Números Reais"""

# Declarar a Variável Real
variavel_real = 3.14
# Imprimir as variáveis na tela (usar .format)
print("O numero é: {}".format(variavel_real))

"""###3. Texto e Comentário"""

# Declarar a Variável tipo String
variavel_string = "Pedro"
# Declarar a Variável tipo Comentário
variavel_comentário = """Este conteúdo foi bem explicado
e desenvolvido de acordo com a máteria"""
# Imprimir as variáveis na tela (usar .format)
print("Meu nome é: {}".format(variavel_string))
print("O Comentário foi: {}".format(variavel_comentário))

# Declarar duas variáveis tipo String
frase_1 = "O meu nome é Pedro, "
frase_2 = "tenho 18 anos"
# Imprimir as frase em um print()
print(frase_1 + frase_2)
print("{}{}".format(frase_1,frase_2))

"""###4. Lógico ou Booleano"""

# Declarar a Variável tipo Boolean
variavel_boolean = True

# Imprimir as variáveis na tela (usar .format)
print("{}".format(variavel_boolean))

"""###5. Lista"""

# Declarar a Variável tipo Lista
variavel_lista = ["Pedro","José", "Carlos", "Bruno"]
# Imprimir as variáveis na tela (usar .format)
print("{}".format(variavel_lista))

"""###6. Dicionário"""

# Declarar a Variável tipo Dicionário
variavel_dicionario = {"Jõao" : "112233", "Pedro" : "223344"}
# Imprimir as variáveis na tela (usar .format)
print("{}".format(variavel_dicionario))

"""## Entrada de dados com INPUT

###1. Texto
"""

# Declarar variável nome
nome = input("Nome: ")
# Imprimir na tela: "Olá Fulano, tudo bem?"
print("Olá " + nome + ", tudo bem?")

"""###2. Número Inteiro"""

# Declarar variável número
numero_1 = int (input("Numero: "))
numero_2 = int(input("Numero: "))
# Imprimir na tela: "Olá Fulano, tudo bem?"
print(numero_1 + numero_2)

"""##Operadores

###1 - Atribuição (=)
"""

# Declarar a variável:
numero = 10
# Imprimir na tela
print(numero)

"""###2 - Adição (+)"""

# Fazer programa que imprime na tela a soma de 2 números
# Declarar a primeira variável:
num_1 = int(input("Entre com o primeiro numero: "))
# Declarar a segunda variável:
num_2 = int(input("Entre com o segundo numero: "))
# Fazer a soma
soma = num_1 + num_2
# Imprimir na tela
print("{} + {} = {}".format(num_1,num_2,soma))
print("Soma = ",soma)

# Fazer programa em que uma variável soma 3 a ela mesma
# Declarar variável
numero = 10
# Fazer a soma dela com 3
# a = a + 3
soma3 = numero = numero + 3
# Imprimir na tela
print(soma3)

"""###3 - Subtração (-)"""

# Fazer programa que imprime na tela a subtração de 2 números
# Declarar a primeira variável:
num_1 = int(input("Digite o primeiro numero: "))
# Declarar a segunda variável:
num_2 = int(input("Digite o segundo numero: "))
# Fazer a subtração
subtração = num_1 - num_2
# Imprimir na tela
print("{} - {} = {}".format(num_1,num_2,subtração))

# Fazer programa em que uma variável subtração 3 a ela mesma
# Declarar variável
numero = 10
# Fazer a subtração dela com 3
subtração3 = numero = numero - 3
# Imprimir na tela
print(subtração3)

"""###4 - Multiplicação (*)"""

# Fazer programa que imprime na tela a multiplicação de 2 números
# Declarar a primeira variável:
num_1 = int(input("Digite o primeiro numero: "))
# Declarar a segunda variável:
num_2 = int(input("Digite o segundo numero: "))
# Fazer a multiplicação
multiplicação = num_1 * num_2
# Imprimir na tela
print("{} * {} = {}".format(num_1,num_2,multiplicação))

# Fazer programa em que uma variável multiplicação 3 a ela mesma
# Declarar variável
numero = 10
# Fazer a multiplicação dela com 3
multiplicação3 = numero = numero * 3
# Imprimir na tela
print(multiplicação3)

"""###5 - Divisão (/)"""

# Fazer programa que imprime na tela a divisão de 2 números
# Declarar a primeira variável:
num_1 = int(input("Digite o primeiro numero: "))
# Declarar a segunda variável
num_2 = int(input("Digite o segundo numero: "))
# Fazer a divisão
divisão = num_1 / num_2
# Imprimir na tela
print("{} / {} = {}".format(num_1,num_2,divisão))

# Fazer programa em que uma variável divisão 3 a ela mesma
# Declarar variável
numero = 12
# Fazer a divisão dela com 3
divisão3 = numero = numero / 3
# Imprimir na tela
print(divisão3)

"""###6 - Módulo (%) -> resto de uma divisão"""

# Fazer programa que imprime na tela o módulo de 2 números
# Declarar a primeira variável:
num_1 = int(input("Digite o primeiro numero: "))
# Declarar a segunda variável:
num_2 = int(input("Digite o segundo numero: "))
# Fazer a módulo
modulo = num_1 % num_2
# Imprimir na tela
print("{} % {} = {}".format(num_1,num_2,modulo))

# Fazer programa em que uma variável módulo 3 a ela mesma
# Declarar variável
numero = 9
# Fazer a módulo dela com 3
modulo3 = numero = numero % 3
# Imprimir na tela
print(modulo3)

"""###7 - Exponenciação (**)"""

# Fazer programa que imprime na tela a exponenciação de 2 números
# Declarar a primeira variável:
num_1 = int(input("Digite o primeiro numero: "))
# Declarar a segunda variável:
num_2 = int(input("Digite o segundo numero: "))
# Fazer a exponenciação
exponenciacao = num_1 ** num_2
# Imprimir na tela
print("{} ** {} = {}".format(num_1,num_2,exponenciacao))

"""###8 - Divisão Inteira (//)"""

# Fazer programa que imprime na tela a divisão inteira de 2 números
# Declarar a primeira variável:
num_1 = int(input("Digite o primeiro numero: "))
# Declarar a segunda variável:
num_2 = int(input("Digite o segundo numero: "))
# Fazer a divisão inteira
divisaointeira = num_1 // num_2
# Imprimir na tela
print("{} // {} = {}".format(num_1,num_2,divisaointeira))

"""##Exercícios

###1. Fazer programa que converte a velocidade de m/s para km/h. Dado: velocidade(m/s) = velocidade(km/h) * 3.6
"""

# Declaração da variável velocidade
velocidade = float(input("Digite uma velocidade(m/s): "))
conversao = velocidade / 3.6
# Imprimir na tela a velocidade convertida
print(conversao , "(km/h)")

"""###2. Fazer um programa em que o usuário digita o raio de um circunferência e o programa imprime na tela o seu comprimento."""

# Importação da biblioteca math
import math as math
# Declaração da variável
raio = float(input("Digite o raio da circunferência: "))
# Calcular o comprimento
comprimento = 2 * math.pi * raio
# Imprimir na tela
print("Comprimento = ", comprimento)

"""###3. Fazer um programa em que o usuário entra com um número e o programa imprime na tela seu antecessor e seu sucessor."""

# Declaração da variável
numero = int(input("Digite um numero: "))
# Calcular o antecessor
Antecessor = numero - 1
# Calcular o sucessor
Sucessor = numero + 1
# Imprimir na tela
print("Antecessor = ", Antecessor , "\nSucessor = ", Sucessor)

"""###4. Fazer um programa em qeue o usuário entra com o ano de seu nascimento e o programa imprime na tela sua idade."""

# Declaração da variável
ano = int(input("Digite o seu ano de nascimento: "))
# Calcular aniversário
idade = 2022 - ano
# Imprimir na tela o aniversário
print("Sua idade é:" ,idade)
