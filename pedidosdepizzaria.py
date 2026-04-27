print("Bem vindo a pizzaria!")
t = input("Qual tamanho você gostaria ? P, M or G: ")
bill = 0

if t == 'P':
    bill = 15
if t == 'M':
    bill = 20
if t == 'G':
    bill = 25

print("Você gostaria de algum adicional, tem interrese?")
pepperoni = input("gostaria de pepperoni? [s/n]")
if pepperoni == 's': 
    if t == 'P':
        bill += 2
    elif t == 'M' or 'G':
        bill += 3
queijo = input ("gostaria de queijo? [s/n]")
if queijo == 's':
    bill += 1

print (f"O total do seu pedido é:{bill}" )
