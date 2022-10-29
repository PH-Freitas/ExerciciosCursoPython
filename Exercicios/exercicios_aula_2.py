"""exercicios_aula_2
#SEGUNDA AULA DE PYTHON

##1 - Operadores Lógicos
Diferente dos operadores aritméticos, os operadores lógicos retornam **True** 😀 ou **False** 😠 como resposta.

###Operadores Relacionais
São aqueles que fazem a comparação entre dois ou mais valores.

####1. Operador de igualdade (==)
"""
# Colocar 7 == 7, verificar a resposta na execussão do programa;
print(7 == 7)
# Colocar 7 == 5, verificar a resposta na execussão do programa;
print(7 == 5)

"""####2. Operadores menor que (<) e maior que (>)

"""

# Colocar 7 < 7, verificar a resposta na execussão do programa;
print(7 < 7)
# Colocar 7 < 10, verificar a resposta na execussão do programa;
print(7 < 10)
# Colocar 7 > 7, verificar a resposta na execussão do programa;
print(7 > 7)
# Colocar 7 > 5, verificar a resposta na execussão do programa;
print(7 > 5)

"""####3. Operadores menor ou igual que (<) e maior ou igual que (>)"""

# Colocar 7 <= 7, verificar a resposta na execussão do programa;
print(7 <= 7)
# Colocar 7 <= 10, verificar a resposta na execussão do programa;
print(7 <= 10)
# Colocar 7 >= 7, verificar a resposta na execussão do programa;
print(7 >= 7)
# Colocar 7 >= 5, verificar a resposta na execussão do programa;
print(7 >= 5)

"""####4. Operador de diferente (!=)"""

# Colocar 7 != 7, verificar a resposta na execussão do programa;
print(7 != 7)
# Colocar 7 != 5, verificar a resposta na execussão do programa;
print(7 != 5)

"""##2 - Tabelas Verdade
São tabelas que mostram algumas situações de entrada e suas saídas

####1. Tabela do E (AND)
O operador **AND** deve ser usado quando temos 2 ou mais condições que devem ser verdadeiras para o programa executar a ação desejada
"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False and False,"|")
print("|",True,"\t|",False,"|",True and False,"|")
print("|",False,"|",True,"\t|",False and True,"|")
print("|",True,"\t|",True,"\t|",True and True,"\t|")

# EXEMPLO: Verificar se uma idade é maior do que a 17 E menor do que 71.

idade = int(input("Idade: "))
print(idade > 17 and idade < 71)

"""####2. Tabela do OU (OR)
O operador **OR** deve ser usado quando, pelo menos, 1 das condições for verdadeira para realizar uma ação desejada
"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False or False,"|")
print("|",True,"\t|",False,"|",True or False," |")
print("|",False,"|",True,"\t|",False or True," |")
print("|",True,"\t|",True,"\t|",True or True," |")

# EXEMPLO: Verificar se uma idade é menor do que a 18 OU maior do que 70.

idade = int(input("Idade: "))
print(idade < 18 or idade > 70)

"""####3. Tabela do XOR (^)"""

print("|   A\t|   B\t| SAÍDA |")
print("|",False,"|",False,"|",False ^ False,"|")
print("|",True,"\t|",False,"|",True ^ False,"\t|")
print("|",False,"|",True,"\t|",False ^ True,"\t|")
print("|",True,"\t|",True,"\t|",True ^ True,"|")

# Reprodução de porcos
# Coloque 0 para leitão e 1 para leitoa em uma lista
leitao = 0
porquinha = 1
filhote = leitao ^ porquinha
print(filhote)

"""####4. Tabela de Negação (not)"""

print("|   A\t| Não A |")
print("|",False,"|",not False,"\t|")
print("|",True,"\t|",not True,"|")

"""##3 - Condicionais

#### Condição SE (IF)
Usamos este tipo de condicional quando necessitamos que o programa teste algumas condições. Caso a condição seja verdadeira, o programa executará uma ação destinada àquela condição.

```
if condição 1:
    bloco de códigos do if

```
Faz-se necessário que o código tenha esta estrutura, senão o Python apresentará erro de identação.
"""

n = 3
if n == 2:
    print("{} igual a 2".format(n))

"""#### Condição SENÃO (ELSE)
Para usar o else, temos que ter usado o if antes.
```
if condição 1:
    bloco de códigos do if
    
else:
    bloco de código do else.
    Aqui finaliza a condicional
```
"""

n = 3
if n == 2:
    print("{} igual a 2".format(n))
else:
    print("{} diferente a 2".format(n))

"""#### Condição SENÃO SE (ELIF)
O elif deve ser utilizado quando temos mais do que uma condição.


```
if condição 1:
    bloco de códigos do if

elif condição 2:
    bloco de código do elif
    
else:
    bloco de código do else.
    Aqui finaliza a condicional
```


"""

ano_nascimento = int(input("Digite seu ano de nascimento\n"))
idade = 2022 - ano_nascimento
if idade < 12:
  print("criança")
elif idade >= 12 and idade <=18:
     print("Aborrecente")
elif idade >= 18 and idade <=35:
     print("Jovem adulto")
elif idade >= 35 and idade <=50:
     print("Adulto começando a ficar velho") 
elif idade >= 50 and idade <=100:
     print("Melhor idade para viver")
else:
     print("Procure o hospital mais próximo")

"""##4 - Exercícios

###1 - Qual o maior.
*Escreva um programa que recebe 2 valores e devolve o maior entre eles.*
"""

# Declaração da variável 1
x = int(input("Digite um número:\n"))
# Declaração da variável 2
y = int(input("Digite um numero:\n"))
# Imprimir na tela mensagem: "O X é maior do que o Y"
if x > y:
  print(x)
else:
  print(y)

"""### 2 - Calculadora de preço da laranja.
*Cada laranja custa R\$ 0,3. Mas quando compradas acima de uma dúzia, seu valor cai para R\$ 0,25 cada*
"""

# Declarar a entrada da quantidade de laranjas a ser comprada
qlaranja = int(input("Digite a quantidade de laranjas a ser comprada: "))
# Declaração de if
if qlaranja >= 12:
   plaranja = 0.25
   resultado = qlaranja * plaranja
   print("{} * {} = {}".format(qlaranja,plaranja,resultado))
# Declaração else
else:
  plaranja = 0.3
  resultado = qlaranja * plaranja
  print("{} * {} = {}".format(qlaranja,plaranja,resultado))
# Imprimir na tela a mensagem: "x laranjas por Y reais totaliza: R$ Z"

"""###3 - Caluladora de Peso Ideal 
Fazer uma calculadora em que o usuário digita Altura em metros e Peso em quilos e se é do sexo biológico Masculino ou Feminino. O programa devolve ao usuário a informação qual seu peso ideal e quando precisa emagrecer para chegar lá. 
Ao final, o programa deve trazer uma frase motivadora para aqueles que estão acima do peso, frase parabenizando os que estão no peso ideal e uma outra frase de alerta aos que estão abaixo do peso.
***Fórmulas***

        >Masculino: (72.7 * Altura) - 50
        >Feminino: (62.1 * Altura) - 44.7

"""

# Declarar a entrada da Altura
altura = float(input("Digite sua altura:\n"))
# Declarar a entrada do Peso
peso = float(input("Digite seu peso:\n"))
# Declarar a entrada do Sexo Biológico
sexo = input("Digite seu sexo biológico\n")
# Declaração de if para calcular peso ideal
if sexo == "masculino" :
   pesoideal = (72.7 * altura) - 50
# Declaração de elif para calcular peso ideal
elif sexo == "feminino" :
     pesoideal = (62.1 * altura) - 44.7
# Declaração else
else:
     print('Erro!')
# Calcular diferença entre peso ideal e peso atual
diferençam = pesoideal - altura * peso 
diferençaf = pesoideal - altura * peso
# Declaração de if para acima do peso - A devolutiva para o usuário vem dentro do if
acimadopeso = altura * peso
if pesoideal < acimadopeso :
  print("Você está acima do peso, mas não se preocupe, com foco você consegue mudar isso !!!")
# Declaração de elif para abaixo do peso - A devolutiva para o usuário vem dentro do elif
elif pesoideal > acimadopeso:
  print("Você está abaixo do peso, mas não se preocupe, com foco você consegue mudar isso !!!")
# Declaração de else - A devolutiva para o usuário vem dentro do else
else:
  print("Voce está no peso ideal")

"""###4 - É triangulo ou Não é triângulo?
Para determinar se 3 segmentos de reta formam um triângulo, podemos fazer a verificação se a soma dos dois menores segmentos é maior do que o segmento maior.

---
    Segmentos: 2, 3 e 4
    Soma dos dois menores: 2 + 3 = 5
    Verificação: 5 > 4
    Conclusão:Estes segmentos formam um triângulo
---
"""

# Declaração do primeiro segmento
seg1 = int(input("Digite o primeiro segmento:\n"))
# Declaração do segundo segmento
seg2 = int(input("Digite o segundo segmento:\n"))
# Declaração do terceiro segmento
seg3 = int(input("Digite o terceiro segmento:\n"))
# Neste if, usar AND para avaliar se o 1º segmento é o menor
if seg1 > seg2 and seg1 > seg3:
   veri = seg3 + seg2
   print("O segmento 1 é o maior")
# Neste elif, usar AND para avaliaar se o 2º segmento é o maior
elif seg2 > seg1 and seg2 > seg3:
   veri = seg1 + seg3
   print("O segmento 2 é o maior")
# Neste elif, usar AND para avaliar se o 3º segmento é o maior
elif seg3 > seg1 and seg3 > seg2:
   veri = seg1 + seg2
   print("O segmento 3 é o maior")
# Else para possíveis erros de digitação
else:
   print("Erro de digitação!!!")
# Verificação se é triângulo e informar ao usuário.
if(veri > max(seg1,seg2,seg3)):
   print("Estes segmentos formam um triângulo!")
else:
   print("Estes segmentos não formam um triângulo!")