n1 = float(input("Digite o nº da tabuada (ela irá até o 10) que deseja ver:"))
if n1 != float(int(n1)) or n1 < 0:
    print("digite um nº inteiro e positivo!")
else:
    print(f"Tabuada do {int(n1)}:")
    for i in range(0,11):
        resultado = n1 * i
        print(f"{(int(n1))} x {i} = {int(resultado)}")

print ("Fim da tabuada! Obrigado por usar nosso sistema!")