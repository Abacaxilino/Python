import random

while True:
    qtd = float(input("digite a quantidade de nº a ser gerada: "))
    if 10 <= qtd <= 100:
        break
    print ("Valor inválido! Digite um valor entre 10 e 100.")
        
numeros = []

for i in range (int (qtd)):
    num = random.randint(1, 1000)
    numeros.append(num)

print (f"os números gerados são {numeros}")
    
