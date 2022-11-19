# -*- coding: utf-8 -*-
"""exercicios_aula_5.ipynb
#Listas
Vetores, conjunto de valores que são alocados em uma única variável.<br>
**Importante:** Listas são definidas pelos [ ]

lista = ['String', 1, 2, 3, True, 2.311, ['batatinha', 'frita', 123]]
"""

lista1 = [
    ['Pao', 200, 0.65],
    ['Queijo', 1000, 50],
    ['Manteiga', 100, 15]
]
print(lista1)

#          0      1      2      3      4      5      6      7      8      9      10     11
meses = ['Jan', 'Fer', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
meses[1:6] # O último numero é exclusivo e o primeiro é inclusivo

numero = list(range(0,11,2))
print(numero)
print(type(numero))

lista = list("O Pedro é legal")
print(lista)

"""## Random
Biblioteca para criar números aleatórios.
## Randint
Comando para gerar numeros inteiros aleatórios.
Neste comando tanto a quanto b são incluídos no range

---
numero = randint(a,b)

---

"""

from random import randint
numeros = []
for i  in range(101):
    numeros.append(randint(0,100))

print(numeros)

"""##Append()
Este método ou função serve para adicionarmos valores a lista
O append adiciona apenas 1 elemento por vez.<br>

---
lista.append('elemento a ser adicionado')

---

## Count()
Este método irá contar quantas ocorrências temos em um determindado elemento.

##len()
Contar quantos elementos temos em uma lista.

Método para saber o comprimento de uma lista.
"""

print(len(numeros))
print(numeros.count(100))

for i in range(len(numeros)):
  print(numeros.count(i))

"""## Para juntar mais de uma lista
## Concatenação de listas
União de elementos de diversas listas

---
'''
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
'''

---

## Extend()
Permite a inclusão de elementos em uma lista
"""

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista1.extend(lista2)
print(lista1)

"""### Sort()
Ordenamento da lista

---
'''
lista.sort()
lista.sort(reverse=True)
'''

---
"""

print(numeros)
#(numeros.sort())
(numeros.sort(reverse=True))

"""## Tabela ASCII
###ord
Comando que converte um caracter em seu número de referência na tabela ASCII
###chr
converte um número inteiro em seu caractere correspondente na tabela ASCII
"""

ord("a")
##chr(90)
##for i in range(200):
    ##print(chr(i))

"""##Exercício 1:
Criar uma lista com todas as letras minúsculas do alfabeto
"""

for a in range(97,123):
    ##print(chr(a))
  listaalf = [chr(a)]
  print(listaalf)

"""### Exercício 2
Transcrever a mensagem do usuário de letras para números.
"""

mencod = []
codmen = []
men = input("Digite uma mensagem:\n")
for cod in  men:
    # Verificar se o número inteiro está entre 97 e 123.
    # Se tiver: append na lista da saída do numero + 3
    # Se não tiver: append do número na lista
    if ord(cod) >= 97 and ord(cod) <= 123:
        mencod.append(ord(cod))
    else:
         mencod.append(ord(cod))
# Printando a saída
print(mencod)
 # converter a nova lista em caracteres novamente e printar na tela
for doc in mencod:
    codmen.append(chr(doc))
print(codmen)

"""#Utilizando String como saída.<br>"""

entrada = list(input("Mensagem: "))
chave = int(input("Entre com a chave de conversão: "))
saida = ""

for letra in entrada:
    num = ord(letra)
    # Verificar SE o número inteiro está entre 97 e 122.
    if num >= 97 and num <= 122:
        # Se tiver: append na lista da saída do número + 3
        num += chave
        if num > 122:
            num -= 26
        saida += chr(num)
        # Se não tiver: append do número na lista
    else:
        saida += chr(num)

# Printando a saída
print(saida)

"""# Set
Set é uma coleção de elementos sem repetição.
Para criar um set, podemos:

#Importante: O set é definido utilizando {}

set_lista = set(lista)

s = {1,2,2,3,3,3,3,3,5,5,8,8}

print(s)

type(s)
"""

set_lista = set(lista)
###s = {1,2,2,3,3,3,3,3,5,5,8,8}
##print(s)
##type(s)


print(numeros)
print(len(numeros))
s = set(numeros)
print(s)
print(len(s))

"""##Tupla
Lista de elementos não iterável. ou seja, não é possível incluir ou excluir elementos dela. IMPORTANTE: Tupla é definida utilizando ( )

---
tupla = (1,5,4,3,8)

---
"""

tupla = (1,5,4,3,8)
print(tupla.count(0))
print(tupla[3:15])
lista = list(tupla[3:35])
print(lista)

print(len(tupla))

"""# Dicionário
### Importante: Definimos dicionários utilizando{}

dicionário = {
  'chave' : 'valor',
    1 : 2,
  'Joao' : True
}


"""

receita = {
    'jan': 100,
    'fev': 120,
    'mar': 100
}
receita ['abr'] = 300
novo_elemento = {'mai': 250}
receita.update(novo_elemento)

for chave, valor in receita.items():
    print(f'{chave} : {valor}')

"""# Criar um dicionário com 3 logins e 3 senhas

###Buscar neste dicionário se os logins e senhas estão corretos
"""

usuarios = {
    'pedro' : '123',
    'drepo' : '321',
    'clovis' : '444'
}
login = input("Login\n").casefold()
senha = input("Senha\n").casefold()
for chave, password in usuarios.items():
    if chave == login and password == senha:
       print("Usuario conectado")
       break
    else:
       print("Usuario e/ou Senha incorreta")
       break