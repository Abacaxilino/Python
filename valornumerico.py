import sys


try :
    n1 = int(input("Digite um número: "))
except ValueError:
    print("valor digitado não é um número inteiro")
    sys.exit("encerrando o programa")

if n1 % 2 == 0:
    print("O número é par")
else: 
    print("O número é impar")