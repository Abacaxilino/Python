# contador inteligente
n1 = int (input ("digite o valor inicial: "))
n2 = int (input ("digite o valor final: "))

if n1 < n2 :
    for c in range (n1 , n2 + 1):
        print (c)

elif n1 > n2 :
        for c in range (n1 , n2 - 1, -1):
            print (c)

elif n1 == n2 :
     print ("não há intervalo para contagem ")

else:
    print ("erro ")

print ('fim do programa! ')