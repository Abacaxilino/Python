while True:
    num =   (float (input('Digite um número:' )))
    if num < 2:
        print("Digite um nº > ou ≡ 2:")
    elif num >= 2:
            for i in range(int(num), -1, -1):     
                 print (i)
            break
print ("contagem finalizada!")
