## Faça um Programa que leia 1 número e, em seguida, informe ao usuário se o número é: Par ou ímpar e Positivo ou negativo;
num = int(input("Digite um número\n"))
if num % 2 == 0:
    print('Numero Par')
else :
    print('Numero Ímpar')
if num >= 0:
    print('Numero Positivo')
else:
    print('Numero Negativo')