"""Desafio
Um posto de gasolina está vendendo combustíveis com a seguinte tabela de descontos: Gasolina:

Até 20 litros: desconto de 4% por litro
Acima de 20 litros: desconto de 6% por litro

Álcool:

Até 20 litros: desconto de 3% por litro
Acima de 20 litros: desconto de 5% por litro

Escreva um programa que leia o tipo de combustível (A - Álcool e G - Gasolina), calcule e imprima o valor a ser pago pelo cliente.

PARA TORNAR O DESAFIO INTERESSANTE, VAMOS FAZER O PROGRAMA CRIAR UM NÚMERO ALEATÓRIO PARA O ABASTECIMENTO. ESTE NÚMERO DEVERÁ SER ENTRE 1 E 52
"""
import random
numA = random.randint(1,52)
numG = random.randint(1,52)
litroA = 3.98
litroG = 4.86
descontoA4 = litroA - (litroA * 4/100)
descontoA6 = litroA - (litroA * 6/100)
descontoG4 = litroG - (litroG * 4/100)
descontoG6 = litroG - (litroG * 6/100)
print(numA)
print(numG)
if numA <= 20:
    print("(Alcool)Voce irá pagar:" , round(numA * descontoA4, 2) ,'reais')
else:
    print("(Alcool)Voce irá pagar:" , round(numA * descontoA6, 2), 'reais')
if numG <= 20:
    print("(Gasolina)Voce irá pagar:" , round(numG * descontoG4, 2), 'reais')
else:
    print("Gasolina)Voce irá pagar:" , round(numG * descontoG6, 2), 'reais')