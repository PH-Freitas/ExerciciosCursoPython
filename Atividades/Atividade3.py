### Fazer uma calculadora com as 4 operações básicas 
# (+ - * /)

x = float(input("Digite um numero:\n"))
y = float(input("Digite outro numero\n"))
resa = x + y
ress = x - y
resm = x * y
resd = x / y
op = input("Adição = 1\nSubtração = 2\nMultiplicação = 3\nDivisão = 4\nDigite o numero correspondente com a operação que deseja realizar:\n")

if(op == "1"):
     print("{} + {} = {}".format(x,y,resa))
elif(op == "2"):
     print("{} - {} = {}".format(x,y,ress))
elif(op == "3"):
     print("{} * {} = {}".format(x,y,resm))
elif(op == "4"):
     print("{} / {} = {}".format(x,y,resd))
else:
     print("Erro!!!")