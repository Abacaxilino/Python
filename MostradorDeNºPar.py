while True: 
    n1= float(input("digite um nº >= 10: "))
       
    if n1 >= 10:
       
        print (f"esses são os nº pares {int(n1)} até 0:") 
        
        for i in range(int(n1), -2, -2 ):

            print(i)
        break
    else:
        print("digite um nº maior ou ≡ 10!") 

print ("Fim de exibição!")