#Calculadora simples

n1 = float(input ("digite o primeiro nº: "))
n2 = float(input ("digite o segundo nº: "))
operador = input ("digite o operador (+, -, *, /): ") 
if operador != " +, -, *, /" :
    print("operador inválido!")
elif operador == "+":
    resultado = n1 + n2
    print ("o resultado é:", resultado)
elif operador == "-":
    resultado = n1 - n2
    print ("o resultado é:", resultado)
elif operador == "*":
    resultado = n1 * n2
    print(" o resultado é:", resultado)
elif operador == "/":
    if n2 != 0:
        resultado = n1 / n2
        print("o resultado é:", resultado)
    else:
        print("erro: divisão por zero não é permitida,")
  


  


    
