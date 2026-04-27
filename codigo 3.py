input ("informe seu e-mail: ")
input ("digite sua data de nascimento (DD/MM/AAAA): ")
senha = input ("crie sua com minímo de 8 caracteres: ")
# while cria um looping de repetição até a condição ser cumprida (Verdadeira)
# len verifica o tamanho ou comprimento de uma Str (linha)
while len(senha) < 8:
    print ("senha muito curta, por favor, cumpra os requisitos! ")
    senha = input ("tente novamente:")
while len(senha) > 8:
    print ("senha excede o limite de caracteres, por favor cumpra os requisitos")
    senha = input ("tente novamente: ")

print ('conta registrada com sucesso!')