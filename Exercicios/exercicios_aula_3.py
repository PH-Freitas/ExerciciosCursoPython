# -*- coding: utf-8 -*-
"""exercicios_aula_3.ipynb

2.	Sabendo que a = 3, b = 7 e c = 4, informe se as expressões abaixo são verdadeiras ou falsas:
a.	(a + c) > b
b.	b > = (a + 2)
c.	c == (b – a)
d.	(b + a) < = c
e.	(c + a) > b
"""

a = 3
b = 7
c = 4
if(a + c) > b:
  print("true")
else:
  print("False")

if(b >= (a+2)):
  print("true")
else:
  print("False")

if(c == (b - a)):
  print("true")
else:
  print("False")

if(b + a) <= c:
  print("true")
else:
  print("False")
  
if((c + a) > b):
  print("true")
else:
  print("False")

"""3.	Sabendo que a = 5, b = 4, c = 3 e d = 6, informe se as expressões abaixo são verdadeiras ou falsas:
a.	(a > c) AND (c <= d)
b.	(a + b) > 10 OR (a + b) == (c + +d)
c.	(a >= c) AND (d >= c)
d.  (b + a) < = c
e.  (c + a) > b
"""

a = 5
b = 4
c = 3
d = 6
if((a>c) and (c<=d)):
  print("True")
else:
  print("False")
if((a+b)>10 or (a+b) == (c + d)):
    print("True")
else:
  print("False")
if((a>=c) and (d>=c)):
    print("True")
else:
  print("False")
if((b+a) <= c):
  print("True")
else:
  print("False")
if((c+a) > b):
  print("True")
else:
  print("False")

"""4. Vamos a um caso mais real...
Meta de vendas: 50.000 unidades.
Usuário vai informar quantas unidades do
produto foram vendidas.


  Se a meta não for atingida, o programa deverá informar que a meta não foi atingida e ninguém recebe bonus.
  Se a meta for atingida com menos de 500 unidades de diferença, o programa informa que a meta foi atingida e que os vendedores ganharão 5% de bonus.
  Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%

"""

x = int(input("Digite a quantidade de produtos vendidos\n"))
if(x < 50_000):
  print("A meta não foi atingida e ninguém receberá bonus !")
elif(x >= 50_000 and x < 50.500):
  print("Parabéns a meta foi atingida e os vendedores receberão 5% de bonus!")
else:
  print("Parabéns, os vendedores receberão 15% de bonus")

"""5. Uma empresa possui 2 produtos: caixa de som e caneca. <br>
A caixa de som custa R\$ 150,00 e a caneca custa R\$ 30,00. <br>
Sabendo que os custos fixos da loja são R\$ 2100.<br>

   Calcule o faturamento dessa loja e se obteve lucro ou prejuizo. O usuário irá informar quantas canecas e quantas caixas de som foram vendidas.
"""

cds = int(input("Digite quantas caixas de som foram vendidas\n"))
cnc = int(input("Digite quantas canecas foram vendidas\n"))
pcds = cds * 150
pcnc = cnc * 30
custofixo = 2100
balanco = pcds + pcnc - custofixo
if(balanco > 0):
  print("A empresa teve lucro !!\n:)")
elif(balanco == 0):
  print("Estamos na média\n:|")
else:
  print("A empresa prescisa melhorar\n:(")

num = input("Digite um numero real:\n")

num = num.replace(",",".")
num = float(num)

print(num)